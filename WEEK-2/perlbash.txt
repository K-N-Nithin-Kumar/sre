-----------------------------------------Bash bash1.sh script -----------------------------------

#!/bin/bash

echo "highest requested Host,upstream_ip,requested path,"
highest_req()
{
Highreqhost=awk -vFPAT='([^" "]*)|("[^"]+")' -vOFS=" " '{if(count[$15]++ >= max) max = count[$15]} END {for ( i in count ) if(max == count[i]) print i, count[i] }' access.log
Highupstream=awk -vFPAT='([^" "]*)|("[^"]+")' -vOFS=" " '{if(count[$9]++ >= max) max = count[$9]} END {for ( i in count ) if(max == count[i]) print i, count[i] }' access.log
Highreqpath=awk -vFPAT='([^" "]*)|("[^"]+")' -vOFS=" " '{if(count[$5]++ >= max) max = count[$5]} END {for ( i in count ) if(max == count[i]) print i, count[i] }' access.log
}


if [ $# -eq 2 ]
then
awk -vFPAT=‘([^” “]*)|(“[^”]+”)’ -vOFS=, -v date1=“$1” -v date2=“$2” \
‘BEGIN{max1;max2=0}
{
	split($2,a,”:”);
	if(date1<a[1]&&a[1]<=date2)
	{
		split($7,b,”:”);
		split($4,x,” “);
		split(c[2],d,”/“);
		if(count1[$15]++>=max1)
		{
			max1=count1[$15];
		}
		if(count2[b[1]]++>=max2)
		{
			max2=count2[b[1]];
		}
		if(count3[d[2]][d[3]]++>=max3)
		{
			max3=count3[d[2]][d[3]];
		}
	}
}
END{
		for(i in count1){
			if(max1=count1[i])
			{
				print i;
			}
		}
		for(i in count2){
			if(max2==count2)
			{
				print i;
			}
		}
		for(i in count3){
			for(j in count3[i]){
				if(count3[i][j]==max3){
					printf “/%s/%s/\n”,i,j;
				}
			}
		}
}’ access.log;
elif [ $# -eq 1 ]
then
	max_host=$(grep $1 access.log | awk -vFPAT=‘([^” “]*)|(“[^”]+”)’ -vOFS=, ‘BEGIN{max=0} {if(count[$15]++>max) max=count[$15]} END{for (i in count) if(count[i]==max) print i}’);
	max_ip=$(grep $1 access.log | awk -vFPAT=‘()|()’ -vOFS=, ‘BEGIN{max=0} {split($7,a,”:”); if(count[a[1]]++>=max) max=count[a[1]]} END{for(i in count) if(count[i]==max) print i}’);
	max_path=$(grep $1 access.log | awk -vOFS=/ ‘BEGIN{max=0} {split($5,a,”/“); if(count[a[2]][a[3]]} END{for (i in count) for(j in count[i]) if(count[i][j]==max) print i,j}’);
	echo “highest requested host = $max_host”;
	echo “highest requested upstream ip = $max_ip”;
	echo “highest requested path = /$max_path/“;
else
	echo “enter  one command”
fi






