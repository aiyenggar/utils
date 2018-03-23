DIREC=$1
PWD=`pwd`
cd $DIREC
for file in `ls $DIREC/*.zip`
do 
  unzip $file; 
  rm $file; 
done
cd $PWD
