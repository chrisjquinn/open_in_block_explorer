folder=$HOME/Documents/open_in_block_explorer

cd $folder/

touch whichexplorer.log whichexplorer.error.log

python3 whichexplorer.py >> $folder/whichexplorer.log 2>> $folder/whichexplorer.error.log
