//shifting to javascript synthesis as no panning for html5 audio tag, hence to generate the sound with riffwave.js

var data = [],
		sampleRateHz = 44100,

		//Notes sequence, play with it ;)
		notes = [87, 0, 0, 87, 0, 0, 85, 0, 0, 82, 0, 0, 80, 0, 0, 82, 0, 82, 0, 80, 0, 0, 82, 0, 0, 85, 0, 0, 78, 0, 0, 78, 0, 78, 0],

		//Base Frequency based on the notes
		baseFreq = function(index) {
			var r = 2 * Math.PI * 440.0 * Math.pow(2,(notes[index]-69)/12.0) / sampleRateHz;
			return r;
		};

//Fill up the sound data!!
for(var j = 0; j < 2*sampleRateHz; j++) {
	var l = 2*sampleRateHz / notes.length;
	data[j] = 64 + 32 * Math.round(Math.sin(baseFreq(Math.round(j/l)) * j));
}

//Riffwave stuff
var wave = new RIFFWAVE();
wave.header.sampleRate = sampleRateHz;
wave.header.numChannels = 1;
wave.Make(data);
var audio = new Audio();
audio.src=wave.dataURI;


function generateSineWave(x,y,z,sampleRate)
function simHertz(hz) {
    var audio = new Audio();
    var wave = new RIFFWAVE();
    var data = [];

    wave.header.sampleRate = 44100;

    var seconds = 1;

    for (var i = 0; i < wave.header.sampleRate * seconds; i ++) {
        data[i] = Math.round(128 + 127 * Math.sin(i * 2 * Math.PI * hz / wave.header.sampleRate));
    }

    wave.Make(data);
    audio.src = wave.dataURI;
    return audio;
}

var audio = simHertz(1000);
audio.play();




// SINE WAVE
var sine = []; for (var i=0; i<10000; i++) sine[i] = 128+Math.round(127*Math.sin(i/5));
var wave2 = new RIFFWAVE(sine);
var audio2 = new Audio(wave2.dataURI);

// EFFECT
var effect = []; for (var i=0; i<35000; i++) effect[i] = 64+Math.round(32*(Math.cos(i*i/2000)+Math.sin(i*i/4000)));
var wave3 = new RIFFWAVE();
wave3.header.sampleRate = 22000;
wave3.Make(effect);
var audio3 = new Audio(wave3.dataURI);

// STEREO
var wave4 = new RIFFWAVE();
wave4.header.sampleRate = 22000;
wave4.header.numChannels = 2;
wave4.header.bitsPerSample = 16;
var i = 0;
var stereo = [];
while (i<100000) {
  stereo[i++] = 0;
  stereo[i++] = 0x8000+Math.round(0x7fff*Math.sin(i/25));
}
while (i<200000) {
  stereo[i++] = 0x8000+Math.round(0x7fff*Math.sin(i/100));
  stereo[i++] = 0;
}
wave4.Make(stereo);
var audio4 = new Audio(wave4.dataURI);

function play(audio) {
  if (!audio.paused) { // if playing stop and rewind
    audio.pause();
    audio.currentTime = 0;
  }
  audio.play();
}



function generateTone(freq, balance,sampleRate) {
  var samples = Math.round(sampleRate / freq),
  data = new Float32Array(samples *2),
  var sample, i;

  for (i = 0; i < samples; i++) {
    sample = Math.sin(Math.PI * 2 * i / samples);
    data[i * 2] = sample * (0.5 - balance);
    data[i * 2 + 1] = sample * (0.5 + balance);
  }

  return data;
}