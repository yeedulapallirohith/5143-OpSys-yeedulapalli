#!/bin/bash
WORDFILE="/usr/share/dict/words"
RANDOM=$$;
sed $(echo $RANDOM)"q;d" $WORDFILE

