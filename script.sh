#primeiro parametro IP do servidor
#segundo protocolo 
#terceiro topologia
#quarta quantidade de clientes
#quinta numero do cliente
#sexta a versao do ping
tamanhodopacote=(1000 1500 2000)
tempodeenvio=(0.01 0.02)

teste=`date +"%T"`
while [ $teste != $7 ]
do
teste=`date +"%T"`
done
r1=$((${RANDOM}%98+2))
printf -v r1 "0.%.2d" $r1
sleep $r1

for tamanho in "${tamanhodopacote[@]}";
do
	for intervalo in "${tempodeenvio[@]}";
	do
		echo "" > /home/meruem/Documentos/TrabalhoDesempenhoCoreCerto/$2/$3/$4/$5.txt
		for i in `seq 30`
		do
		echo $tamanho $intervalo
		$6 $1 -i $intervalo -s $tamanho -c 500 >> /home/meruem/Documentos/TrabalhoDesempenhoCoreCerto/$2/$3/$4/$5.txt
		done
		cat /home/meruem/Documentos/TrabalhoDesempenhoCoreCerto/$2/$3/$4/$5.txt | grep rtt | cut -d"/" -f5 >> /home/meruem/Documentos/TrabalhoDesempenhoCoreCerto/$2/$3/$4/$intervalo' - '$tamanho.csv		
	done
done
