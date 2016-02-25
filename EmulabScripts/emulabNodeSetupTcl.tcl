set ns [new Simulator]
source tb_compat.tcl
set serv0 [$ns node]
tb-set-hardware $serv0 d710
tb-set-node-os $serv0  UbuntuJava-Mongo-SQL
set serv1 [$ns node]
tb-set-hardware $serv1 d710
tb-set-node-os $serv1  UbuntuJava-Mongo-SQL
set serv2 [$ns node]
tb-set-hardware $serv2 d710
tb-set-node-os $serv2  UbuntuJava-Mongo-SQL
set serv3 [$ns node]
tb-set-hardware $serv3 d710
tb-set-node-os $serv3  UbuntuJava-Mongo-SQL
set serv4 [$ns node]
tb-set-hardware $serv4 d710
tb-set-node-os $serv4  UbuntuJava-Mongo-SQL
set serv5 [$ns node]
tb-set-hardware $serv5 d710
tb-set-node-os $serv5  UbuntuJava-Mongo-SQL
set serv6 [$ns node]
tb-set-hardware $serv6 d710
tb-set-node-os $serv6  UbuntuJava-Mongo-SQL
set serv7 [$ns node]
tb-set-hardware $serv7 d710
tb-set-node-os $serv7  UbuntuJava-Mongo-SQL
set serv8 [$ns node]
tb-set-hardware $serv8 d710
tb-set-node-os $serv8  UbuntuJava-Mongo-SQL
set serv9 [$ns node]
tb-set-hardware $serv9 d710
tb-set-node-os $serv9  UbuntuJava-Mongo-SQL
set serv10 [$ns node]
tb-set-hardware $serv10 d710
tb-set-node-os $serv10  UbuntuJava-Mongo-SQL
set serv11 [$ns node]
tb-set-hardware $serv11 d710
tb-set-node-os $serv11  UbuntuJava-Mongo-SQL
set serv12 [$ns node]
tb-set-hardware $serv12 d710
tb-set-node-os $serv12  UbuntuJava-Mongo-SQL
set serv13 [$ns node]
tb-set-hardware $serv13 d710
tb-set-node-os $serv13  UbuntuJava-Mongo-SQL
set serv14 [$ns node]
tb-set-hardware $serv14 d710
tb-set-node-os $serv14  UbuntuJava-Mongo-SQL
set serv15 [$ns node]
tb-set-hardware $serv15 d710
tb-set-node-os $serv15  UbuntuJava-Mongo-SQL
set serv16 [$ns node]
tb-set-hardware $serv16 d710
tb-set-node-os $serv16  UbuntuJava-Mongo-SQL
set serv17 [$ns node]
tb-set-hardware $serv17 d710
tb-set-node-os $serv17  UbuntuJava-Mongo-SQL
set serv18 [$ns node]
tb-set-hardware $serv18 d710
tb-set-node-os $serv18  UbuntuJava-Mongo-SQL
set serv19 [$ns node]
tb-set-hardware $serv19 d710
tb-set-node-os $serv19  UbuntuJava-Mongo-SQL
set serv20 [$ns node]
tb-set-hardware $serv20 d710
tb-set-node-os $serv20  UbuntuJava-Mongo-SQL
set serv21 [$ns node]
tb-set-hardware $serv21 d710
tb-set-node-os $serv21  UbuntuJava-Mongo-SQL
set serv22 [$ns node]
tb-set-hardware $serv22 d710
tb-set-node-os $serv22  UbuntuJava-Mongo-SQL
set serv23 [$ns node]
tb-set-hardware $serv23 d710
tb-set-node-os $serv23  UbuntuJava-Mongo-SQL
set serv24 [$ns node]
tb-set-hardware $serv24 d710
tb-set-node-os $serv24  UbuntuJava-Mongo-SQL
set serv25 [$ns node]
tb-set-hardware $serv25 d710
tb-set-node-os $serv25  UbuntuJava-Mongo-SQL
set serv26 [$ns node]
tb-set-hardware $serv26 d710
tb-set-node-os $serv26  UbuntuJava-Mongo-SQL
set serv27 [$ns node]
tb-set-hardware $serv27 d710
tb-set-node-os $serv27  UbuntuJava-Mongo-SQL
set serv28 [$ns node]
tb-set-hardware $serv28 d710
tb-set-node-os $serv28  UbuntuJava-Mongo-SQL
set serv29 [$ns node]
tb-set-hardware $serv29 d710
tb-set-node-os $serv29  UbuntuJava-Mongo-SQL
set serv30 [$ns node]
tb-set-hardware $serv30 d710
tb-set-node-os $serv30  UbuntuJava-Mongo-SQL
set serv31 [$ns node]
tb-set-hardware $serv31 d710
tb-set-node-os $serv31  UbuntuJava-Mongo-SQL
set serv32 [$ns node]
tb-set-hardware $serv32 d710
tb-set-node-os $serv32  UbuntuJava-Mongo-SQL
set serv33 [$ns node]
tb-set-hardware $serv33 d710
tb-set-node-os $serv33  UbuntuJava-Mongo-SQL
set serv34 [$ns node]
tb-set-hardware $serv34 d710
tb-set-node-os $serv34  UbuntuJava-Mongo-SQL
set serv35 [$ns node]
tb-set-hardware $serv35 d710
tb-set-node-os $serv35  UbuntuJava-Mongo-SQL
set serv36 [$ns node]
tb-set-hardware $serv36 d710
tb-set-node-os $serv36  UbuntuJava-Mongo-SQL
set serv37 [$ns node]
tb-set-hardware $serv37 d710
tb-set-node-os $serv37  UbuntuJava-Mongo-SQL
set serv38 [$ns node]
tb-set-hardware $serv38 d710
tb-set-node-os $serv38  UbuntuJava-Mongo-SQL
set serv39 [$ns node]
tb-set-hardware $serv39 d710
tb-set-node-os $serv39  UbuntuJava-Mongo-SQL
set lan0 [$ns make-lan "$serv0 $serv1 $serv2 $serv3 $serv4 $serv5 $serv6 $serv7 $serv8 $serv9 $serv10 $serv11 $serv12 $serv13 $serv14 $serv15 $serv16 $serv17 $serv18 $serv19 $serv20 $serv21 $serv22 $serv23 $serv24 $serv25 $serv26 $serv27 $serv28 $serv29 $serv30 $serv31 $serv32 $serv33 $serv34 $serv35 $serv36 $serv37 $serv38 $serv39"  1000Mbps 0ms]
$ns run
