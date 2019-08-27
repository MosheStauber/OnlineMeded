$video = $args[0]
$url = $args[1]
$end = $args[2]

mkdir $video;

$i = 1;
DO 
{
	youtube-dl -o $("$video/{0:0000}.ts" -f $i) "$url$i$end";
	$i++;
} While ($LASTEXITCODE -eq 0)

# gci '.\Pulmonary Embolism\' | Foreach-Object { echo "file '$($_.FullName)'" >> flist.txt }
# ffmpeg.exe -f concat -safe 0 -i flist.txt -c:v copy out.mp4

#"Sodium" "https://jwpsrv-vh.akamaihd.net/i/content/conversions/Pd1viDFY/videos/2y254pg3-30497135.mp4/segment" "_0_av.ts"
#"Potassium" "https://jwpsrv-vh.akamaihd.net/i/content/conversions/Pd1viDFY/videos/m6upBDRA-30497135.mp4/segment" "_0_av.ts"
#"GI Bleed" "https://videos-f.jwpsrv.com/content/conversions/Pd1viDFY/videos/yF5zXuto-30497135.mp4-" ".ts"
#"Liver Function Tests" "https://jwpsrv-vh.akamaihd.net/i/content/conversions/Pd1viDFY/videos/GXaJ0Ptw-30497135.mp4/segment" "_0_av.ts" 
#"Inpatient Diabetes" "https://jwpsrv-vh.akamaihd.net/i/content/conversions/Pd1viDFY/videos/EBUQjgPT-30497135.mp4/segment" "_0_av.ts