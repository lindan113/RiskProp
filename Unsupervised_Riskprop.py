import numpy as np
import pandas as pd

Transaction_Info = pd.read_csv('./data/Transaction_Information.csv')
Account_Info = pd.read_csv('./data/Account_Information.csv')

Payer_TxNumber = Account_Info["out_degree"]
Payee_TxNumber = Account_Info["in_degree"]


nodes = Account_Info["index"]
node_label = Account_Info["label"]
edges = Transaction_Info["Tx_id"]
Tx_Score = Transaction_Info["de_anonymous_score"]
reliable_0=Account_Info["unsupervised_reliable_0"]

print("ethereum network has %d nodes and %d edges" % (len(nodes), len(edges)))

reliable = dict()
trust = dict()
confidence = dict()
score = dict()


max_Payee_TxNumber =max(Payee_TxNumber)
max_Payer_TxNumber =max(Payer_TxNumber)

print("max_Payee_TxNumber", max_Payee_TxNumber)
print("max_payer_TxNumber", max_Payer_TxNumber)

payer = Transaction_Info['index_from']
payee = Transaction_Info['index_to']


for edge in edges:
    confidence[edge] = 0.5  # confidence的初始化

for node_t in nodes:
    trust[node_t] = 0.5
    reliable[node_t] = reliable_0[node_t]

iter = 0

d_reliable = 0
d_trust = 0
d_confidence = 0

##### ITERATIONS START ######
incount_for_node = dict()
outcount_for_node = dict()
trust_value_all = dict()
reliable_value_all = dict()
for node_t in nodes:
    trust_value_all[node_t] = 0
    reliable_value_all[node_t] = 0

while iter < 400:
    print('-----------------')
    print("Epoch number %d with d_reliable = %f, d_trust = %f, d_confidence = %f" % (
    iter, d_reliable, d_trust, d_confidence))
    if np.isnan(d_reliable) or np.isnan(d_trust) or np.isnan(d_confidence):
        print('over')
        break

    d_reliable = 0
    d_trust = 0
    d_confidence = 0
    ############################################################
    for node_t in nodes:
        trust_value_all[node_t] = 0
        reliable_value_all[node_t] = 0
    print("Calculating Relialbe and trust of accounts by all the edges")
    for edge in edges:
        trust_value_all[Transaction_Info["index_to"][edge]] += Tx_Score[edge] * confidence[edge]
        reliable_value_all[Transaction_Info["index_from"][edge]] += confidence[edge]

    ############################################################
    ############################################################

    print('Updating trust of account')

    for node in nodes:

        payee_txn = Payee_TxNumber[node]
        trust_total = trust_value_all[node]

        if payee_txn > 0.0:
            trust_for_node = trust_total / payee_txn
        else:
            trust_for_node = 0.5

        x = trust_for_node
        if x < 0:
            x = 0
        if x > 1.0:
            x = 1.0
        d_trust += abs(trust[node] - x)
        trust[node] = x

    ############################################################

    print("Updating Relialbe of accounts")

    for node in nodes:
        payer_txn = Payer_TxNumber[node]
        reliable_total = reliable_value_all[node]

        if payer_txn > 0.0:
            reliable_for_node = reliable_total / payer_txn
        else:
            reliable_for_node = reliable_0[node]

        x = reliable_for_node
        if x < 0.00:
            x = 0.0
        if x > 1.0:
            x = 1.0

        d_reliable += abs(reliable[node] - x)
        reliable[node] = x

    ############################################################

    print("Updating confidence of transactions")

    for edge in edges:
        account_from_reliable = reliable[Transaction_Info["index_from"][edge]]
        account_to_trust = trust[Transaction_Info["index_to"][edge]]
        transaction_score = Tx_Score[edge]
        x = (account_from_reliable +  (1 - abs(transaction_score - account_to_trust))) / 2

        if x < 0.00:
            x = 0.0
        if x > 1.0:
            x = 1.0

        d_confidence += abs(confidence[edge] - x)
        confidence[edge] = x

    ###########################################################

    iter += 1
    if d_trust < 0.01 and d_confidence < 0.01 and d_reliable < 0.01:
        print("The propagation equation reaches convergence after " + str(iter) + " more iterations!")
        break
RISK=dict()
for node in nodes:
    RISK[node]=10-10*reliable[node]

fw = open("./results/20220205-Account-trust-reliabl-risk-unsupervised-riskprop.csv", "w")
fw.write("node,trust,reliable,risk\n")

for node in nodes:
    fw.write("%s,%s,%s,%s\n" % (str(node), str(trust[node]), str(reliable[node]),str(RISK[node])))
fw.close()

fw_confidence = open("./results/20220205-Transaction-score-confidence-unsupervised-riskprop.csv", "w")
fw_confidence.write("Transaction,score,confidence\n")

for edge in edges:
    fw_confidence.write("%s,%s,%s\n" % (str(edge), str(confidence[edge]), str(Tx_Score[edge])))
