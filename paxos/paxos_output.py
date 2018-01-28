Proposer 0:  17, Content-47679
Proposer 1:  28, Content-79747
Proposer 2:  74, Content-52168

>> Pre-Accepted by Proposer 0
Accepter 0:  17, None

>> Pre-Accepted by Proposer 1
Accepter 0:  28, None

>> Pre-Accepted by Proposer 0
Accepter 1:  17, None

>> Pre-Accepted by Proposer 1
Accepter 1:  28, None

>> Pre-Accepted by Proposer 0
Accepter 2:  17, None

>> Pre-Accepted by Proposer 1
Accepter 2:  28, None

# 此时 Proposer 0 和 Proposer 1 都未出局
# 但是显然 Proposer 0 的所有提案会在第二阶段被拒绝

>> Refused by Proposer 0
Accepter 0:  28, None

>> Refused by Proposer 0
Accepter 1:  28, None

>> Refused by Proposer 0
Accepter 2:  28, None

# Proposer 0 的所有提案在第二阶段被拒绝

>> Locked by Proposer 1
Accepter 0:  28, Content-79747

# 此时 Proposer 1 锁定了 Accepter 0
# 但是被 Proposer 2 插入

>> Pre-Accepted and updated by Proposer 2
Accepter 0:  74, Content-79747

# Accepter 0 已被锁定
# 把 Proposer 1 的提案 返回给 Proposer 2
# Proposer 2 更新了提案

>> Pre-Accepted by Proposer 2
Accepter 1:  74, None

>> Refused by Proposer 1
Accepter 1:  74, None

>> Pre-Accepted by Proposer 2
Accepter 2:  74, None

>> Refused by Proposer 1
Accepter 2:  74, None

# 此时 Proposer 1 已经无法锁定后两个提案
# 因为 Proposer 2 给出了更大的提案 ID

>> Error: Can not edited at accept_proposal by Proposer 2
Accepter 0:  74, Content-79747

# Proposer 2 无法更改已经被锁定的 Accepter 0

>> Locked by Proposer 2
Accepter 1:  74, Content-79747

>> Locked by Proposer 2
Accepter 2:  74, Content-79747

# Proposer 2 成功锁定后两个 Accepter

>> Broadcast already accept by Proposer 0
Accepter 0:  28, Content-79747

>> Broadcast already accept by Proposer 0
Accepter 1:  74, Content-79747

>> Broadcast already accept by Proposer 0
Accepter 2:  74, Content-79747

# Proposer 2 完成广播，但是其内容是 Proposer 1 的提案

Time: 0.573580s
Accepter 0:  28, Content-79747
Accepter 1:  74, Content-79747
Accepter 2:  74, Content-79747
