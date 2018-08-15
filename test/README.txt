=============================================
|											|
| Voice Recognition Testing Tool			|
|											|
| Developed by Timothy Wong					|
| twong@mobis-usa.com						|
| MTCA Test & Development, Automation Team	|
|											|
| Version 0.5 (Beta)						|
| Updated 8/15/2018							|
|											|
=============================================

0. Release Note
===============
- 8/15/2018
-----------
	. Version 0.5 (Beta) released.
	. Original version of this README complete.

1. Introduction
===============
This tool is developed for the following purposes:
- To standardize the validation of head unit (HU) voice recognition (VR) function.
- To provide a simple way for testing multiple languages (en-US, fr-CA, and es-MX) on HU VR.


2. Hardware Overview and Setup
==============================
- Overview:
	The GUI sends commands to HU through Android Debug Bridge (ADB) to trigger VR function,
	then plays a pre-recorded voice command, which is received by HU. HU then gives a voice output.
	This voice output will be received by our Python program, which interfaces with Google speech recognition.
	The returned text from Google will be verified with an output text to determine the test case result (PASS/FAIL).

- Setup:
	. Obtain a headset with microphone from IT department. Connect it to your PC.
	. Set up your HU with power supply and harness as usual. Make sure the harness also has a microphone attached.
	. Place the headset on top of the power supply dummy box.
	  The microphone from the headset should be directly above the speakers from the dummy box.
	. Secure the microphone from the HU harness between the two earpieces of the headset.
	. Connect HU to PC through ADB USB.
	. Pair 2 phones to the HU through Bluetooth (certain test cases involve switching Bluetooth devices).
	. Add the following 3 names to Bluetooth phone contacts (for Bluetooth phone call test cases):
		John Smith
		Pierre Durant
		Juan Garcia
	  (please use these 3 names; phone numbers can be random). 
	. Perform multiple and POI searches on HU map (certain test cases need multiple search records).


3. Software Overview and Setup
==============================
- Overview:
	This tool is a simple graphical user interface (GUI) developed on Python.
	It targets the top-level VR commands listed under All Menus -> Voice Commands.
	
- Setup:
	. Download the entire folders of "dist", "audio_files", and "expected_output_files".
	. Put the "dist" folder, which contains vrGui6.exe, in your local drive (preferrably somewhere in Z:).
	. Put the "audio_files" folder, which contains .wav audio files, in the following location:
		Z:/Projects/VR_project/audio_files/
	. Put the "expected_output_files" folder, which contains .txt files, to the following location:
		Z:/Projects/VR_project/expected_output_files/
	(Please follow the exact paths when moving audio_files and expected_output_files folders,
	path change and assignment are not implemented as of 8/15/2018.)

	
4. Using the GUI
================
- In the "dist" folder, go into vrGui6, then find and execute vrGui6.exe. 
  The security software on your PC may ask you whether you want to allow or block the application. 
  Always allow the application.

- You should see a blank command prompt window pop up, followed by a VR Test GUI after a few seconds.
  The command prompt window will show information about the GUI operation, such as processes and results;
  the VR Test GUI is where the user would select and run different commands.
  
- There are 4 drop-down menus and a Run button on the GUI.
  
  . The drop-down menu on the top-left allows the user to switch between Local and Server VR modes*,
    depending on whether Blue Link network services are activated on the HU under test.
    (* Note: only Local mode is supported by the GUI as of 8/15/2018.)
	
  . The drop-down menu on the left of the second row allows the user to choose among 3 languages.
    "en-US" -> American English; 
	"fr-CA" -> Canadian French;
	"es-MX" -> Mexican Spanish.
	
  . The drop-down menu in the middle of the second row allows the user to choose among 3 function categories.
    "Navigation" -> Map and navigation functions; requires map SD card.
	"Phone" -> Bluetooth call functions; user should try to pair 2 different phones with the HU.
    "Radio" -> Switches among FM, AM, and SXM radio bands*.
    (* Note: only a fixed channel/frequency is supported in each band as of 8/15/2018.)
	
  . The drop-down menu on the right of the second row allows the user to choose a specific command under 
    current language and category.
	
- After choosing the language, category, and command, the user can click the Run button to send the command to HU.
  Here is a use case example:
  -> User selects en-US, Radio, AM 1080, and clicks Run.
  -> Observe output from the command prompt window.
	  -> Running test case...
		 . This notifies the user that the command is being sent to HU through ADB.
	  -> am1080en
		 . This shows the current test case that is being run.
		 . The audio file "am1080en.wav" will be played as voice input.
		 . The text file "am1080en_out.txt" will be used to verify the result at the end of the test case.
	  -> vrStart
		 . The program executes the vrStart() function to start VR on HU via ADB.
		 . The PC will send the command "adb -s [device_name] input keyevent KEYCODE_SHORTCUT_PTT" to HU.
	  -> vrInput
		 . The program executes the vrInput() function to play a am1080en.wav.
	  -> vrOutput
		 . The program executes the vrOutput() function to receive and process voice output from HU.
	  -> Listening...
		 . Program is waiting for and receiving voice output from HU.
		 . Program sends the received data to be processed by Google speech recognition in the background.
		 . Google speech platform interprets the data and returns an output text string.
	  -> Writing results to <out.txt>...
	     . The returned output text string will be written to the file called "out.txt".
		 . out.txt is located in the same folder as vrGui6.exe.
	  -> Done.
	     . Program has finished writing the results to out.txt. 
  -> The program will then compare the output string in out.txt with the expected string in am1080en_out.txt.
  

5. Test Results
===============
- If the two strings match, the program will output the following text to the command prompt window and another pop-up:
	"VR output matches expected output.
	
	PASS"
	
- If there is any mismatch between the two strings, the program will output the following:
	"VR output does not match expected output.
	(Make sure test conditions are correct, and minimize surrounding noise.)
	
	FAIL"
	
- If, for some reason, Google is unable to interpret the data from HU voice output
  (this could happen if there is too much noise in the surroundings, or the wrong language is chosen, etc.),
  the program will output:
	"Google could not understand audio"
	
- If, for other reasons beyond the scope of this project, Google has encountered an error, the program will output:
	"Google error; [some_error_message]"
  
(Note: If the user finds that certain test results are unexpected, please first see below, 6. Remarks,
before notifying the developer.)


6. Remarks
==========
- Avoid manual interruption between clicking Run button and end of test case:
-----------------------------------------------------------------------------
  . In general, the GUI is quite stable within normal operation. 
  . However, exception and interruption handling has not been implemented on this version of the GUI yet.
    After clicking the Run button, and before the end of test result validation, please do not manually interrupt
	the program (e.g. clicking Run again, clicking the drop-down menus, etc.).
  . Manual interruptions while a test case is running can cause the GUI to crash. In that case the application 
    will have to be restarted.
  . If you realize you need to make changes to the testing conditions after clicking the Run button, simply wait 
    until the test case has finished (it will probably give FAIL as a result) before making changes.

- Incomplete test cases (as of 8/15/2018):
------------------------------------------
  There are certain test cases that show up in the GUI but are not completely implemented.
  Running these test cases will result in a Python error, but the results are still written to "out.txt",
  which is located in the same folder as vrGui6.exe.
  
  The user can consider opening "out.txt" to manually verify the output string for these test cases.
  
  Please pay attention to the following list of test cases that are incomplete:
  
  . en-US, Navigation, Destination information
  . fr-CA, Navigation, Informations de destination
  . es-MX, Navigation, Informacion de destino
    -> These commands returns the distance and ETA from current position to destination.
	-> The output depends on the destination set by the user.

  . en-US, Navigation, Find 46501 Commerce Center Dr, Plymouth, Michigan
  . en-US, Phone, Send message to John Smith
    -> These commands should work when HU Blue Link network is enabled.
	
  . es-MX, Navigation, Encontrar direccion en California
    -> As of 8/15/2018, Spanish HU VR only supports address search in Puerto Rico.
	-> This test case should result in text notifying user that current region is not supported.
	
- Inconsistent/problematic test cases (as of 8/15/2018):
--------------------------------------------------------
  This affects a small subset of commands supported by the GUI.
  The inconsistencies/problems can be caused by flaws on either HU side or Google server side.

  Running these test cases may result in false-positives and false-negatives.
  The user can consider opening "out.txt" to manually verify the output string for these test cases.
  "out.txt" is located in the same folder as vrGui6.exe.
  
  Please pay attention to the following list of test cases that are known to give inconsistent/problematic results:

  . en-US, Navigation, Cancel route
    -> Google always interprets the result as "the round has been canceled".
	-> Expected output is supposed to be "the route has been canceled".
	-> cancelRoute_out.txt has been modified to "the round has been canceled".
	
  . en-US, Navigation, Pause route
    -> Google sometimes interprets the result as "causing ground guidance".
	-> Expected output should be "pausing route guidance".
	-> pauseRoute_out.txt contains the expected output.
	
  . en-US, Navigation, Turn guidance on
  . en-US, Navigation, Turn guidance off
	-> Both HU and Google often confuses the above voice inputs due to similarities in pronunciation.
	
  . en-US, Navigation, Zoom in
    -> Google often interprets the result as "map to men", "Matt Damon", etc.
	-> Expected output is supposed to be "map zoom in".
	-> zoomIn_out.txt has been modified to "map to men".
	
  . en-US, Navigation, Zoom out
    -> Google often interprets the result as "map to Mount".
	-> Expected output is supposed to be "map zoom out".
	-> zoomOut_out.txt has been modified to "map to Mount".
	
  . fr-CA, Navigation, Continuer trajet
    -> Google sometimes interprets the result as "reprendre le guidage du trajets"
	-> Expected output is "reprendre le guidage des trajets"
	
  . fr-CA, Radio, FM 97.1
    -> HU voice output has voice overlap issues.
	-> HU responds correctly by tuning to FM 97.1, but Google often interprets frequency as 97.4.
	-> fm97.1fr_out.txt shows expected output (97.1).
	

	