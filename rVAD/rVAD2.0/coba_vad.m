data = "D:\Mata Kuliah\Tesis\With Data Covid\Data\neg\neg-0421-083-cough-m-53-0.mp3";
loc = "D:\Mata Kuliah\Tesis\a.csv";

[y, fs] = audioread(data);
N = length(y);
time = (1:N);
subplot(2,1,1);
plot(time,y);

vad(data,loc);

m = csvread(loc);
subplot(2,1,2);
plot(1:length(m),m);

disp(length(m));
disp(N/fs);