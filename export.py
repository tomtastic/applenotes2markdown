#!/usr/bin/env python3
"""Python tool to export Apple Notes database entries to markdown files
   eg. Notes databases :
        ~/Library/Containers/com.apple.Notes/Data/Library/Notes/*.storedata
   2022-01-31 - TRCM
"""

import io
import os
import pathlib
import sqlite3
from markdownify import markdownify as md

# https://pypi.org/project/markdownify/


def run(path, output_path, include_tags):
    """Take path to Notes sqlite, output separate Markdown files to output dir"""
    path = os.path.expandvars(path)
    output_path = os.path.expandvars(output_path)

    conn = sqlite3.connect(path)
    cursor = conn.cursor()

    with cursor.execute("select ZFOLDER, ZDATEEDITED, ZBODY, Z_PK from ZNOTE") as row:

        note = {
            "folder_id": row[0],
            # Apple Core Data time starts at 2001-01-01
            "updated": row[1] + 978325200,
            "body_id": row[2],
            "notes_pk": row[3],
        }

        folder_name = cursor.execute(
            f"select ZNAME from ZFOLDER WHERE Z_PK = {note['folder_id']}"
        ).first[0]

        with cursor.execute(
            f"select ZHTMLSTRING from ZNOTEBODY WHERE Z_PK = {note['body_id']}"
        ) as body_row:
            # The Apple database stores stuff in HTML (lol)
            # so we gotta convert it to something human-readable
            # => markdown

            html_text = body_row[0]
            markdown_text = md(html_text, heading_style="ATX")
            if include_tags:
                # markdown_text << "\n\n##{folder_name}"
                pass

            folder_output_path = os.path.join(
                output_path, folder_name, f"{note['notes_pk']}.md"
            )
            general_output_path = os.path.join(
                output_path, "all_notes", f"{note['notes_pk']}.md"
            )

            for full_output_path in [folder_output_path, general_output_path]:

                pathlib.Path(
                    os.path.expandvars(os.path.join("..", full_output_path))
                ).mkdir(parents=True, exist_ok=True)

                with io.open(full_output_path, "w", encoding="utf8") as mf_file:
                    mf_file.write(markdown_text)

                # Change the modified dates to the correct ones
                os.utime(full_output_path, (note["updated"], note["updated"]))

                print(f"Successfully generated {full_output_path}")


if __name__ == "__main__":
    run(
        path="~/Library/Containers/com.apple.Notes/Data/Library/Notes/*.storedata",
        output_path="./fx_export/",
        include_tags=True,
    )
