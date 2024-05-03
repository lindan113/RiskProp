# RiskProp


## 1.English Version

Dataset Discription
(1) Dataset Name:
	Risk propagation of Ethereum transactions

(2) Description  
	Our work shares phishing account information from Etherscan. In addition, we share the RiskPro algorithm for detection in our work (RiskProp: Account Risk Rating on Ethereum via De-anonymous Score and Network Propagation).  
We crawled the phishing accounts in Ethereum from December 1, 2019 to December 31, 2019 and their first-order and second-order nodes from https://etherscan.io/accounts/label/phish-hack, and got a total of 243 phishing accounts. Due to the limitation of memory size, we collect 10 accounts with recent transactions from these first-order nodes, and collect all the first-order neighborhood of these selected accounts as the second-order nodes.The second-order transaction network of phishing nodes consists of  1.19 million accounts and 4.13 million transactions.

(3) Update Log
	We crawled the phishing accounts in Ethereum from December 1, 2019 to December 31, 2019 

(4) Contents
	a. all_hash_0_hop_803_labels.csv
	Discription: this file contains the information of training and testing accounts, and it is used for result vertification.

	-Column：
		1. index：index of account
		2. Address: address of account
		3. discription: description of  account type
		4. label: label of account e.g., label of illicit account is 1, label of licit account is 0.
		sum：4 columns
	-Row：
		each row represents an account.
	
	b. all_hash_0_hop_643_labels.csv
	Discription: this file contains the information of training  accounts, and it is used for the input of training accounts' label when doing supervised experiment.
	
	-Column：
		1. index：index of account
		2. Address: address of account
		3. discription: description of  account type
		4. label: label of account e.g., label of illicit account is 1, label of licit account is 0
		sum：4 columns
	-Row：
		each row represents an account.
	
	c. Transaction_Information.csv
	-Column：
		1. Tx_id: index of transaction
		2. address_from: address of payer
		3. address_to: address of payee
		4. index_from: index of payer
		5. index_to: index of payee
		6. de_anonymous_score: de_anonymous_score of transaction
		7. random_score: random_score of transaction
		sum：7 columns
	-Row：
		each row represents a transaction.
	
	d. Account_Information.csv
	-Column：
		1. index: index of account
		2. out_degree: payments number of account
		3. in_degree: receptions number of account
		4. all_degree: transaction number of account
		5. label: label of account
		6. unsupervised_reliable_0: initial reliable of account in unsupervised experiment
		7. supervised_reliable_0: initial reliable of account in supervised experiment
	-Row：
		each row represents an account.

(5) Citation
	updating...
	BibTex
	IEEE
	ACM
(6) Contact
	updating...
	Please contact  () for any questions about the dataset

Code Discription
(1)Requirements
To run this code fully, you will need these repositories. We have been running our code in Python 3.7.
	numpy == 1.21.2
	pandas == 1.3.5

(2)Contents
	a. Supervised_Riskprop.py 
		This script will calculate account risk rating using RiskProp method with the dataset which contains 643 labled accounts and around 1.19 million unlabeled accounts.
	b. Unsupervised_Riskprop.py
		This script will calculate account risk rating using RiskProp method with the dataset which contains around 1.19 million unlabeled accounts.

===============================================================================================================================================

## 2.中文版

数据集信息
(1) 名称：
	以太坊交易风险传播

(2) 简介：

	a. 数据来源：从 https://etherscan.io 爬取了到的目标节点相关交易数据. 
	b. 数据研究对象：以太坊
	c. 数据集大小：该二阶交易网络数据集为从Etherscan上爬取的243个目标钓鱼节点以及560个非钓鱼节点的二阶交易网络信息。由于内存受限，选择了和一阶节点发生的最近的交易中的10个账户，并将这10个账户的一阶邻居作为二阶节点。在该二阶交易网络中有119万个账户和414万条交易。
	d. 研究工作：《RiskProp: Account Risk Rating on Ethereum via De-anonymousScore and Network Propagation》

(3) 更新时间：

	数据集是从2019年12月1日到2019年12月31日目标账户最近的10000条交易数据（若不足10000条则统计全部交易）

(4) 内容：

	a. all_hash_0_hop_803_labels.csv
	描述：该文件包含了训练集和测试集的账户信息，用于实验结果验证。
	
	-列：
		1. index：账户的序号
		2. Address: 账户的地址
		3. discription: 账户的类型描述
		4. label:账户的标签，非法账户的标签为1，正常账户的标签为0。
		总和：4列
	-行：
		每一行代表一个账户信息
	
	b. all_hash_0_hop_643_labels.csv
	描述：该文件包含了训练集的账户信息，用于在监督实验中输入训练集的标签信息。
	
	-列：
		1. index：账户的序号
		2. Address: 账户的地址
		3. discription: 账户的类型描述
		4. label:账户的标签，非法账户的标签为1，正常账户的标签为0
		总和：4列
	-行：
		每一行代表一个账户信息
	
	c.Transaction_Information.csv
	-列：
		1. Tx_id：交易的序号
		2. address_from: 转账账户的地址
		3. address_to: 入账账户的地址
		4. index_from: 转账账户的序号
		5. index_to: 入账账户的序号
		6. de_anonymous_score: 交易的去匿名分数
		7. random_score: 交易的随机分数
		总和：7列
	-行：
		每一行代表一次交易信息
	
	d.Account_Information.csv
	-列：
		1. index: 账户的序号
		2. out_degree: 账户的转账次数
		3. in_degree: 账户的入账次数
		4. all_degree: 账户的交易次数
		5. label: 账户的标签
		6. unsupervised_reliable_0: 无监督实验的账户可靠度初始值
		7. supervised_reliable_0: 监督实验的账户可靠度初始值
	-行：
		每一行代表一个账户信息

(5) 引用格式：
	待更新...
	BibTex
	IEEE
	ACM

(6) 联系人：
	待更新...
	若对数据集有任何问题请联系  (@mail2.sysu.edu.cn)。

代码信息

(1)Requirements
我们使用Python3.7以及下面两个第三方库：
	numpy == 1.21.2
	pandas == 1.3.5

(2)内容

	a. Supervised_Riskprop.py 
		这个代码文件输入了643个有标签账户和大约119万个无标签账户，使用RiskProp模型计算出所有账户的风险级别。
	
	b. Unsupervised_Riskprop.py
		这个代码文件输入了大约119万个无标签账户，使用RiskProp模型计算出所有账户的风险级别。

