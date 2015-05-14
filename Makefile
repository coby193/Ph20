Ph20Set4Latex.tex: Ph20Set3OscillatorFigure1.png Ph20Set3ErrorPlot.png Ph20Set3hcomparison.png Ph20Set3Energies.png Ph20Set3ImplicitErrors.png Ph20Set3ExplicitPhase.png Ph20Set3ImplicitPhase.png Ph20Set3SymplecticPhase.png Ph20Set3SymplecticEnergy1.png Ph20Set3SymplecticEnergy2.png Ph20Set3PhaseComparison.png
	pdflatex Ph20Set4Latex.tex
Ph20Set3OscillatorFigure1.png: Makefile Ph20Set3Oscillator.py 
	python Ph20Set3Oscillator.py Ph20Set3OscillatorFigure1.png 0 1 .0001 5 plot
Ph20Set3ErrorPlot.png: Makefile Ph20Set3Oscillator.py
	python Ph20Set3Oscillator.py Ph20Set3ErrorPlot.png 0 1 .0001 5 errors
Ph20Set3hcomparison.png: Makefile Ph20Set3Oscillator.py
	python Ph20Set3Oscillator.py Ph20Set3hcomparison.png 0 1 .0016 5 hcomparison
Ph20Set3Energies.png: Makefile Ph20Set3Oscillator.py
	python Ph20Set3Oscillator.py Ph20Set3Energies.png 0 1 .0001 5 energy
Ph20Set3ImplicitErrors.png: Makefile Ph20Set3Oscillator.py 
	python Ph20Set3Oscillator.py Ph20Set3ImplicitErrors.png 0 1 .0001 5 impliciterror
Ph20Set3ExplicitPhase.png: Makefile Ph20Set3Oscillator.py
	python Ph20Set3Oscillator.py Ph20Set3ImplicitPhase.png 0 1 .01 5 expphase
Ph20Set3ImplicitPhase.png: Makefile Ph20Set3Oscillator.py
	python Ph20Set3Oscillator.py Ph20Set3ImplicitPhase.png 0 1 .01 5 impphase
Ph20Set3SymplecticPhase.png: Makefile Ph20Set3Oscillator.py
	python Ph20Set3Oscillator.py Ph20Set3SymplecticPhase.png 0 1 .01 5 symphase
Ph20Set3SymplecticEnergy1.png: Makefile Ph20Set3Oscillator.py
	python Ph20Set3Oscillator.py Ph20Set3SymplecticEnergy1.png 0 1 .01 5 symenergy
Ph20Set3SymplecticEnergy2.png: Makefile Ph20Set3Oscillator.py
	python Ph20Set3Oscillator.py Ph20Set3SymplecticEnergy2.png 0 1 .1 5 symenergy
Ph20Set3PhaseComparison.png: Makefile Ph20Set3Oscillator.py
	python Ph20Set3Oscillator.py Ph20Set3PhaseComparison.png 0 1 .01 5 phasecheck
