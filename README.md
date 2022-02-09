# applenotes2markdown
Python tool to export Apple Notes database entries to markdown files

### 2022 (MacOS Monterey 12.3)
- Database has moved to `~/Library/Group Containers/group.com.apple.notes/NoteStore.sqlite`
- Schemas have changed, a lot.
- Folder and Note titles seem are in table `ZICCLOUDSYNCINGOBJECT`
- If Note is encrypted, the note data is stored in table `ZICNOTEDATA`, with note `Z_PK` from `ZICCLOUDSYNCINGOBJECT` as field `ZNOTE`
- Selecting _non-deleted_ folders : `select Z_PK, ZTITLE2 from ZICCLOUDSYNCINGOBJECT where (ZMARKEDFORDELETION=0 and ZNEEDSINITIALFETCHFROMCLOUD=0 and length(ZTITLE2)>=1)`
- Selecting all _non-deleted_ notes from a given folder_z_pk : `select Z_PK, ZTITLE1 from ZICCLOUDSYNCINGOBJECT where (ZMARKEDFORDELETION=0 and ZNEEDSINITIALFETCHFROMCLOUD=0 and ZFOLDER=%folder_z_pk%)`
- Timestamps seem to be : `ZCREATIONDATE3, ZMODIFICATIONDATE1`
