C='white'
T='solo-confio-en-localhost'
ORG=$(T).org
PIN=$(T).pin
PDF=$(T).pdf
CC='../fonts/cc-icons.ttf'
FONT='../fonts/Inconsolata.otf'

run: org2pin
	pinpoint $(PIN)

pdf:
	pinpoint $(PIN) -o $(PDF)

org2pin:
	echo "[font=Inconsolata 60px]" >$(PIN)
	echo "[text-color=#80c800]" >>$(PIN)
	echo "[shading-opacity=0.000001]" >>$(PIN)
	echo "[black]" >>$(PIN)
	egrep -v "^#\+[A-Z_]+:" $(ORG) | sed 's/^\*\+/--\n/g' \
	| sed 's/2>&1//g' \
	| sed 's/2&>1//g' \
	| sed 's/#+RESULTS://g' \
	| sed "s/#+BEGIN_.*/\<span foreground='#ffff00'\>\<b\>/g" \
	| sed 's/#+END_.*/\<\/b\>\<\/span\>/g' \
	| sed 's/&$$//g' >>$(PIN)

pub: pdf
	scp $(PDF) osiux:~/pub/charlas
	ssh osiux 'cd pub && ln -s charlas/$(PDF)'

all: org2pin pdf pub

