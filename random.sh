find . -type f -exec md5 '{}' ';' | sort | uniq -f 3 -d | sed -e "s/.*(\(.*\)).*/\1/“ |  xargs rm

flatten a directory and mv files
find TargetDirectory/ -mindepth 2 -type f -exec mv -i '{}' TargetDirectory/ ';'

find ~/Music/iTunes/iTunes\ Media/ -type f -mindepth 2 -exec cp '{}’ ~/sangeetham/ ‘;'

find . -name "* 2.mp3" -exec rm '{}' ‘;'
