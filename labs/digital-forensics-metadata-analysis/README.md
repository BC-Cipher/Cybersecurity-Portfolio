# Digital Forensics & Metadata Analysis

**Environment:** Kali Linux  
**Tools:** ExifTool, FFmpeg, Linux Command Line  
**Focus:** Metadata Analysis, Timestamp Validation, Geolocation, Video Forensics

## Overview

During cybersecurity competition preparation, I practiced examining digital video evidence to identify metadata, analyze timestamps, interpret geographic coordinates, and inspect individual video frames.

I compared metadata and timestamps before drawing conclusions from the video evidence.

## 1. File Metadata Examination

Used ExifTool to inspect embedded metadata and identify potentially useful information, including:

- File properties and media format
- Creation and modification timestamps
- Recording device information
- GPS coordinates
- Software and encoding information

**Commands practiced:**

```bash
exiftool filename.mov
exiftool -a -u -G1 filename.mov
```

The second command provides a more detailed examination, including duplicate metadata tags, unknown tags, and their associated metadata groups.

## 2. Timestamp Analysis

Examined multiple timestamp fields and compared their possible meanings.

**Key lesson:** A file's modification date, media container creation date, and original recording date may differ.

Understanding these differences is important when determining the timeline of a digital investigation.

**Command practiced:**

```bash
exiftool -a -G1 -time:all filename.mov
```

## 3. Geolocation Analysis

Explored GPS metadata embedded in digital media and learned how geographic coordinates can provide investigative context.

Practiced interpreting latitude and longitude in degrees, minutes, and seconds and converting them into decimal-degree format.

**Command practiced:**

```bash
exiftool -a -G1 -gps:all filename.mov
```

GPS metadata can help identify where a recording device reported its location, but its accuracy and reliability must be evaluated.

## 4. Video Frame Extraction

Used FFmpeg to extract still images from video footage for closer visual examination.

**Command practiced:**

```bash
ffmpeg -i filename.mov -vf fps=2 frame_%03d.png
```

This command extracts two frames per second and saves them as numbered PNG images.

## 5. Embedded Text Examination

Explored the use of the Linux `strings` utility to identify human-readable text embedded within a media file.

**Command practiced:**

```bash
strings -a filename.mov
```

This technique can reveal useful textual information, although results must be interpreted carefully.

## Lessons Learned

- Metadata can provide valuable information about digital evidence.
- Different timestamps may reflect different events in a file's history.
- GPS information requires interpretation and validation.
- Video frames may provide visual context that metadata cannot.
- Combining several investigative techniques produces more reliable findings than relying on one tool.

## Professional Applications

The techniques practiced are relevant to digital forensics and incident response, cybersecurity investigations, evidence examination, OSINT, and security analysis.

## Learning Context

This entry documents general technical skills developed during cybersecurity competition preparation. It does not include competition-specific questions, answers, artifacts, or confidential information.
