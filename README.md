**************************************************************************
        
		FFT (Fast Fourier Transform) SOFTWARE USAGE
		
		
Created by Maria Pedrosa Bustos (mpedrosab@gmail.com)
    on 16-03-2021 for the Department of Applised Physics (UGR)
	
**************************************************************************

There are two versions of the software:
	FFT_Full: Calculate the FFT, store the data in a text file and PLOT it. (Compatible with latest Windows versions) 
	FFT_noPlot: The same but DOES NOT plot the data. (Compatible with almost all Windows versions)
	
If "FFT_Full" does not work, try "FFT_noPlot".


**INSTRUCTIONS**

1. Unzip the file "FFT.rar"
2. Place your data file inside the same directory as the ".exe" file you want to use. 
	DO NOT CHANGE THE LOCATION OF THE EXE FILE OR ANY OTHER FOLDER INSIDE THE SOFTWARE DIRECTORY!
3. Run the ".exe" and follow the instructions.
4. Results are stored inside the "Output" folder.

NOTES:
    * Zero point is removed to avoid singularities.
    * Assumes that the time interval between samples is constant along the whole data.

	* Input file must be a raw text file with two columns: time (s) and data. 
		Header labels can be none or any that contains a "T". All text before a line containing "T" are ignored.
		Example of a valid header:
		
	                 _______________________________________________
			|   Posición angular-canales 1 y 2, Ensayo #1   |	<- This line is ignored
			|   Tiempo ( s )	Posición angular ( rad )|
			|   0,0000	000000                          |
			|   0,0100	000000                          |
			|   ...      ...                                |
			|_______________________________________________|	                                        
							
		Another example: 
			 _______________________________________________	
			|	Time	Velocity                        |	
                        |	0,0000	000000                          |
                        |	0,0100	000000                          |
                        |	...      ...                            |
                        |_______________________________________________|


		No headers:
			 _______________________________________________
			|	0,0000	000000                          |
		        |	0,0100	000000                          |
	                |	...      ...                            |
                        |_______________________________________________|
						
						
**UPDATES**

v1.2:
	-Input data can have empty rows at the end.
	-Errors are now shown on terminal instead of directly closing the window when a problem occurs
	
