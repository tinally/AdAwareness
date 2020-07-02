#!/bin/bash

while read line
do 
	php view_extraction.php $line >> $2

done < $1 
