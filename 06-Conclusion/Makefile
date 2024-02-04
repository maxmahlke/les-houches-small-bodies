latex:
	pdflatex *.tex
	mv main.pdf 2024-LesHouches-OnlineTools.pdf

clean:
	rm *bbl *aux *nav *out *dvi *snm *toc *blg *log *~ sections/*~ sections/*log

distribute:
	qpdf --split-pages=14 2024-LesHouches-OnlineTools.pdf output-%d.pdf
	mv output-01-14.pdf ../04-Data_Access/4.0-Data_Access.pdf
	qpdf --split-pages=8 output-15-27.pdf output-%d.pdf
	mv output-01-08.pdf ../05-Spectra_Access/5.0-Spectra_Access.pdf
	mv output-09-13.pdf 6.0-Conclusion.pdf
	rm output-15-27.pdf
