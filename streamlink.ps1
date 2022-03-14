#!/usr/bin/pwsh

param([Parameter(Mandatory=$true)]$auth,
[Parameter(Mandatory=$true)]$clientid,
[Parameter(Mandatory=$true)]$url,
[Parameter(Mandatory=$true)]$output)

$strDate = $(Get-Date -UFormat "%Y%m%d-%H%mL")

$useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53"
$output = "/home/grimdark/Music/podcasts/raw$output-original-$strDate.mp3"
$ffmpeg = "aac"
$command = "/home/grimdark/.local/bin/streamlink"
$args =  '--http-header Authorization=$auth --http-header Client-Id=$clientid --http-header User-Agent=$useragent --output $output --ffmpeg-verbose --ffmpeg-audio-transcode $ffmpeg $url audio'

Invoke-Expression "python3 $command $args"