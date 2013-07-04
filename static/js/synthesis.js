//Shifting to javascript synthesis as no panning for html5 audio tag, hence to generate the sound with riffwave.js

/*Experiment to generate random location and sound corresponding to those location.
    The following attributes of sound are used to map the 3D location of the  real world:
        Y-Axis or Height (on the scale of 1 10 ) : with increasing Pitch of sound.
        X-Axis or Direction (Left or Right scale of -5 0 5) : Panning of sound on the 2 channel.
        Z-Axis or Depth (on scale of 1 10 ) : with amplitude of sound for each channel difference of 3dB for each step.
    The produce soundScape for location is being used for training.
    A random test is conducted to check the accuracy of these mapping on Blindfolded people.
    Furthermore Color is also represented using different frequency for each sound.
*/

//function for 3D point
function Point(x,y,z){
    this.x=x;
    this.y=y;
    this.z=z;
}

function generateSineWave(point,sampleRate,amp){
    var wave4 = new RIFFWAVE();   //riffwave variable
    var data = [];
    var seconds = 1;
    wave4.header.sampleRate = sampleRate;
    wave4.header.numChannels = 2;
    wave4.header.bitsPerSample = 16;
    var pitch = [440,466,494,523,554,587,622,659,698,740,784,831,880];   //predefined notes in hz
    var frequencyHz = pitch[point.y];
    var amplitude = amp*point.z;
    var balance = point.x/10;

    //generation of data for tone
    for (var i = 0; i < wave.header.sampleRate * seconds; i ++) {
        sample = Math.round(128 + 127 * Math.sin(i * 2 * Math.PI * frequencyHz / wave.header.sampleRate)*amplitude);
        //setting the pan for each channel
        data[i++] = sample * (0.5 - balance);
        data[i++] = sample * (0.5 + balance);
    }
    wave4.Make(data);
    var audio4 = new Audio(wave4.dataURI);
    return audio;
}

function test(){
    alert("in test");
    var point = new Point(1,0,0);
    var audio = generateSineWave(point,44100,1000);
    audio.play();
}

function Experiment(mode){
    switch (mode){
        case "Training":
            break;
        case "Testing":
            break;
    }
    var audio = generateSineWave(1000);
    audio.play();
}

/*
function play(audio) {
  if (!audio.paused) { // if playing stop and rewind
    audio.pause();
    audio.currentTime = 0;
  }
  audio.play();
}*/
 /*var data = [],
		sampleRateHz = 44100,

		//Notes sequence, play with it ;)
		notes = [87, 0, 0, 87, 0, 0, 85, 0, 0, 82, 0, 0, 80, 0, 0, 82, 0, 82, 0, 80, 0, 0, 82, 0, 0, 85, 0, 0, 78, 0, 0, 78, 0, 78, 0],

		//Base Frequency based on the notes
		baseFreq = function(index) {
			var r = 2 * Math.PI * 440.0 * Math.pow(2,(notes[index]-69)/12.0) / sampleRateHz;
			return r;
		};

*/
