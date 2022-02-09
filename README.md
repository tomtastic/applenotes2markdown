# applenotes2markdown
Python tool to export Apple Notes database entries to markdown files

### 2022 (MacOS Monterey 12.3)
- Database has moved to `~/Library/Group Containers/group.com.apple.notes/NoteStore.sqlite`
- Schemas have changed, a lot.
- Folder and Note titles seem are in table `ZICCLOUDSYNCINGOBJECT`
- Selecting _non-deleted_ folders : `select Z_PK, ZTITLE2 from ZICCLOUDSYNCINGOBJECT where (ZMARKEDFORDELETION=0 and ZNEEDSINITIALFETCHFROMCLOUD=0 and length(ZTITLE2)>=1)`
- Selecting all _non-deleted_ notes from a given folder_z_pk : `select Z_PK, ZTITLE1 from ZICCLOUDSYNCINGOBJECT where (ZMARKEDFORDELETION=0 and ZNEEDSINITIALFETCHFROMCLOUD=0 and ZFOLDER=%folder_z_pk%)`
- Timestamps seem to be : `ZCREATIONDATE3, ZMODIFICATIONDATE1`
