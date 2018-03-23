DIREC=$1
#DIREC="$HOME/data/20171226-patentsview"
PWD=`pwd`
cd $DIREC
for file in `ls $DIREC/*.zip`
do 
  unzip $file; 
  rm $file; 
done
cd $PWD
