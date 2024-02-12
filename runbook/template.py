TEMPLATES = {}

# PYTHON_TEMPLATE_START
# 2024-02-11T18:07:50-08:00
TEMPLATES[
    "python"
] = """
ewogImNlbGxzIjogWwogIHsKICAgImNlbGxfdHlwZSI6ICJtYXJrZG93biIsCiAgICJpZCI6ICJlMzY4MDEzYiIsCiAgICJtZXRhZGF0YSI6IHsKICAgICJlZGl0YWJsZSI6IHRydWUsCiAgICAic2xpZGVzaG93IjogewogICAgICJzbGlkZV90eXBlIjogIiIKICAgIH0sCiAgICAidGFncyI6IFtdCiAgIH0sCiAgICJzb3VyY2UiOiBbCiAgICAiIyBUSVRMRVxuIiwKICAgICIjIyBEZXNjcmlwdGlvbiIKICAgXQogIH0sCiAgewogICAiY2VsbF90eXBlIjogIm1hcmtkb3duIiwKICAgImlkIjogIjMwZDlkY2I5IiwKICAgIm1ldGFkYXRhIjogewogICAgImVkaXRhYmxlIjogdHJ1ZSwKICAgICJzbGlkZXNob3ciOiB7CiAgICAgInNsaWRlX3R5cGUiOiAiIgogICAgfSwKICAgICJ0YWdzIjogW10KICAgfSwKICAgInNvdXJjZSI6IFsKICAgICIjIyBTZXR1cCIKICAgXQogIH0sCiAgewogICAiY2VsbF90eXBlIjogImNvZGUiLAogICAiZXhlY3V0aW9uX2NvdW50IjogbnVsbCwKICAgImlkIjogIjE5ZWY2OTAzLTJmY2QtNGJkZi05MzVlLTkyY2UyOTQwYjI3NyIsCiAgICJtZXRhZGF0YSI6IHsKICAgICJ0YWdzIjogWwogICAgICJwYXJhbWV0ZXJzIgogICAgXQogICB9LAogICAib3V0cHV0cyI6IFtdLAogICAic291cmNlIjogWwogICAgIiMgUEFSQU1FVEVSUyBERUZBVUxUU1xuIiwKICAgICJkcnlfcnVuID0gVHJ1ZSAgIyBjb250cm9scyBzaCBiZWhhdmlvciBmb3Igc2FmZXR5IgogICBdCiAgfSwKICB7CiAgICJjZWxsX3R5cGUiOiAiY29kZSIsCiAgICJleGVjdXRpb25fY291bnQiOiBudWxsLAogICAiaWQiOiAiYTFkYjg1ZDUtODlhNC00NzIxLTgzN2MtMmYxN2Y1NTU4MWViIiwKICAgIm1ldGFkYXRhIjogewogICAgInRhZ3MiOiBbXQogICB9LAogICAib3V0cHV0cyI6IFtdLAogICAic291cmNlIjogWwogICAgIiMgU0hFTEwgSEVMUEVSU1xuIiwKICAgICJmcm9tIHJ1bmJvb2suc2hlbGwgaW1wb3J0IHNoZWxsX2J1aWxkZXIsIGdhdGhlciwgY29uZmlybSwgc3R5bGUsIHF1b3RlXG4iLAogICAgIlxuIiwKICAgICJzaCA9IHNoZWxsX2J1aWxkZXIoXG4iLAogICAgIiAgICBkcnlfcnVuLCB0YWdzX2RlZmF1bHQ9e1wiZW52aXJvbm1lbnRcIjogXCJ0ZXN0aW5nXCJ9LCBjb25maXJtX2RlZmF1bHQ9VHJ1ZVxuIiwKICAgICIpIgogICBdCiAgfSwKICB7CiAgICJjZWxsX3R5cGUiOiAiY29kZSIsCiAgICJleGVjdXRpb25fY291bnQiOiBudWxsLAogICAiaWQiOiAiYjYwYjZlNzEtMTNkYS00MGQzLTlhNzQtMDE2Zjc1ZmJhZjQ2IiwKICAgIm1ldGFkYXRhIjogewogICAgInRhZ3MiOiBbXQogICB9LAogICAib3V0cHV0cyI6IFtdLAogICAic291cmNlIjogWwogICAgIiMgV2lkZ2V0c1xuIiwKICAgICJpbXBvcnQgaXB5d2lkZ2V0cyBhcyB3aWRnZXRzXG4iLAogICAgImZyb20gSVB5dGhvbi5kaXNwbGF5IGltcG9ydCBkaXNwbGF5XG4iLAogICAgIlxuIiwKICAgICJ3ID0gd2lkZ2V0cy5Ecm9wZG93bihcbiIsCiAgICAiICAgIG9wdGlvbnM9WyhcIlByb2R1Y3Rpb25cIiwgMSksIChcIlN0YWdpbmdcIiwgMiksIChcIkRldmVsb3BtZW50XCIsIDMpXSxcbiIsCiAgICAiICAgIHZhbHVlPTMsXG4iLAogICAgIiAgICBkZXNjcmlwdGlvbj1cIkVudmlyb25tZW50OlwiLFxuIiwKICAgICIpXG4iLAogICAgIlxuIiwKICAgICJ2ID0gd2lkZ2V0cy5Ecm9wZG93bihcbiIsCiAgICAiICAgIG9wdGlvbnM9W1wiTXlzcWxcIiwgXCJSZWRpc1wiLCBcIk1lbWNhY2hlZFwiXSxcbiIsCiAgICAiICAgIHZhbHVlPVwiUmVkaXNcIixcbiIsCiAgICAiICAgIGRlc2NyaXB0aW9uPVwiRGF0YWJhc2U6XCIsXG4iLAogICAgIilcbiIsCiAgICAiZGlzcGxheSh3KVxuIiwKICAgICJkaXNwbGF5KHYpIgogICBdCiAgfSwKICB7CiAgICJjZWxsX3R5cGUiOiAiY29kZSIsCiAgICJleGVjdXRpb25fY291bnQiOiBudWxsLAogICAiaWQiOiAiNzliMTgwNzYtMzQwZi00MmQzLWEwMjEtOTZhNjYxZGU3ZTNhIiwKICAgIm1ldGFkYXRhIjoge30sCiAgICJvdXRwdXRzIjogW10sCiAgICJzb3VyY2UiOiBbCiAgICAicHJpbnQoZlwiVmFsdWUgb2Ygd2lkZ2V0OiB7dy52YWx1ZX0ge3YudmFsdWV9XCIpIgogICBdCiAgfSwKICB7CiAgICJjZWxsX3R5cGUiOiAibWFya2Rvd24iLAogICAiaWQiOiAiZjc2MTAyOTgiLAogICAibWV0YWRhdGEiOiB7CiAgICAiZWRpdGFibGUiOiB0cnVlLAogICAgInNsaWRlc2hvdyI6IHsKICAgICAic2xpZGVfdHlwZSI6ICIiCiAgICB9LAogICAgInRhZ3MiOiBbXQogICB9LAogICAic291cmNlIjogWwogICAgIiMjIE9wZXJhdGlvbiIKICAgXQogIH0sCiAgewogICAiY2VsbF90eXBlIjogIm1hcmtkb3duIiwKICAgImlkIjogImFkZjJkYzNjIiwKICAgIm1ldGFkYXRhIjoge30sCiAgICJzb3VyY2UiOiBbCiAgICAiIyMjIFN0ZXAgMSAtIEdldCBnaXQgaW5mbyIKICAgXQogIH0sCiAgewogICAiY2VsbF90eXBlIjogImNvZGUiLAogICAiZXhlY3V0aW9uX2NvdW50IjogbnVsbCwKICAgImlkIjogIjZlZTEyNjYxLTYyYjgtNDNiNy1iNTU3LTJhY2M5YTM0NmQ4NCIsCiAgICJtZXRhZGF0YSI6IHt9LAogICAib3V0cHV0cyI6IFtdLAogICAic291cmNlIjogWwogICAgIm91dHB1dCA9IGF3YWl0IHNoKFwiZ2l0IC0tdmVyc2lvbiAmJiBlY2hvIDMzMyA+JjJcIiwgY29uZmlybT1UcnVlKSIKICAgXQogIH0sCiAgewogICAiY2VsbF90eXBlIjogIm1hcmtkb3duIiwKICAgImlkIjogIjgyYzkwNjE0IiwKICAgIm1ldGFkYXRhIjogewogICAgImVkaXRhYmxlIjogdHJ1ZSwKICAgICJzbGlkZXNob3ciOiB7CiAgICAgInNsaWRlX3R5cGUiOiAiIgogICAgfSwKICAgICJ0YWdzIjogW10KICAgfSwKICAgInNvdXJjZSI6IFsKICAgICIjIyMgU3RlcCAyIC0gUHJpbnQiCiAgIF0KICB9LAogIHsKICAgImNlbGxfdHlwZSI6ICJjb2RlIiwKICAgImV4ZWN1dGlvbl9jb3VudCI6IG51bGwsCiAgICJpZCI6ICI1Yzk0NTQ4Zi0yMTk3LTRkZTctYjcyYy1iMWZlYjI5YmMxOGMiLAogICAibWV0YWRhdGEiOiB7fSwKICAgIm91dHB1dHMiOiBbXSwKICAgInNvdXJjZSI6IFsKICAgICJwcmludChvdXRwdXQpIgogICBdCiAgfSwKICB7CiAgICJjZWxsX3R5cGUiOiAibWFya2Rvd24iLAogICAiaWQiOiAiZjBlOWVhZGUiLAogICAibWV0YWRhdGEiOiB7fSwKICAgInNvdXJjZSI6IFsKICAgICI8c3BhbiBzdHlsZT0nY29sb3I6IHJlZDsnPjxib2xkPkRBTkdFUjwvYm9sZD48L3NwYW4+IDxzcGFuIHN0eWxlPSdjb2xvcjogcmVkOyc+PGJvbGQ+REFOR0VSPC9ib2xkPjwvc3Bhbj4gPHNwYW4gc3R5bGU9J2NvbG9yOiByZWQ7Jz48Ym9sZD5EQU5HRVI8L2JvbGQ+PC9zcGFuPiAgVGhlIGZvbGxvd2luZyBjb2RlIGlzIGdvaW5nIHRvIGJlIHJpc2t5LiBCZSBwcmVwYXJlZCB3aXRoIHJvbGxiYWNrIHByb2NlZHVyZXMuIgogICBdCiAgfSwKICB7CiAgICJjZWxsX3R5cGUiOiAiY29kZSIsCiAgICJleGVjdXRpb25fY291bnQiOiBudWxsLAogICAiaWQiOiAiMGFkZDI4MTYtYTljYi00MTBjLTgzZjMtYTRhYWQ2YWFmZjVmIiwKICAgIm1ldGFkYXRhIjoge30sCiAgICJvdXRwdXRzIjogW10sCiAgICJzb3VyY2UiOiBbCiAgICAiY29uZmlybShzdHlsZShcIkRhbmdlciwgcmVhZHkgdG8gcHJvY2VlZD9cIiwgZmc9XCJyZWRcIiwgYm9sZD1UcnVlKSwgYWJvcnQ9VHJ1ZSlcbiIsCiAgICAiY21kcyA9IFtzaChcInNsZWVwIDE7IGVjaG8gMVwiKSwgc2goXCJzbGVlcCAyOyBlY2hvIDJcIiksIHNoKFwic2xlZXAgMzsgZWNobyAzXCIpXSIKICAgXQogIH0sCiAgewogICAiY2VsbF90eXBlIjogImNvZGUiLAogICAiZXhlY3V0aW9uX2NvdW50IjogbnVsbCwKICAgImlkIjogImVmNTI1YjZkLTIwNTktNDEyZS1hMGNiLWMxZTkwOGNhNTRjNyIsCiAgICJtZXRhZGF0YSI6IHt9LAogICAib3V0cHV0cyI6IFtdLAogICAic291cmNlIjogWwogICAgInJlc3VsdCA9IGF3YWl0IGdhdGhlcigqY21kcykiCiAgIF0KICB9LAogIHsKICAgImNlbGxfdHlwZSI6ICJtYXJrZG93biIsCiAgICJpZCI6ICI3NGQ5NDFmMiIsCiAgICJtZXRhZGF0YSI6IHt9LAogICAic291cmNlIjogWwogICAgIiMjIENsZWFudXAiCiAgIF0KICB9LAogIHsKICAgImNlbGxfdHlwZSI6ICJtYXJrZG93biIsCiAgICJpZCI6ICJkNWIxNmRiZSIsCiAgICJtZXRhZGF0YSI6IHsKICAgICJlZGl0YWJsZSI6IHRydWUsCiAgICAic2xpZGVzaG93IjogewogICAgICJzbGlkZV90eXBlIjogIiIKICAgIH0sCiAgICAidGFncyI6IFtdCiAgIH0sCiAgICJzb3VyY2UiOiBbCiAgICAiIyMgUm9sbGJhY2siCiAgIF0KICB9LAogIHsKICAgImNlbGxfdHlwZSI6ICJtYXJrZG93biIsCiAgICJpZCI6ICIzZTM3ODRmYy1lMDczLTQ5YTMtYTE3ZC1jNWY4MjczMzk0YjAiLAogICAibWV0YWRhdGEiOiB7CiAgICAiZWRpdGFibGUiOiB0cnVlLAogICAgInNsaWRlc2hvdyI6IHsKICAgICAic2xpZGVfdHlwZSI6ICIiCiAgICB9LAogICAgInRhZ3MiOiBbXQogICB9LAogICAic291cmNlIjogWwogICAgIiMjIEFjdGlvbiBJdGVtcyAvIExlYXJuaW5ncyIKICAgXQogIH0sCiAgewogICAiY2VsbF90eXBlIjogImNvZGUiLAogICAiZXhlY3V0aW9uX2NvdW50IjogbnVsbCwKICAgImlkIjogImFkN2VkNTFmLTdlMGYtNGM3ZC05NWIzLWM3M2VjZGVhYTNhOCIsCiAgICJtZXRhZGF0YSI6IHsKICAgICJ0YWdzIjogW10KICAgfSwKICAgIm91dHB1dHMiOiBbXSwKICAgInNvdXJjZSI6IFtdCiAgfQogXSwKICJtZXRhZGF0YSI6IHsKICAia2VybmVsc3BlYyI6IHsKICAgImRpc3BsYXlfbmFtZSI6ICJQeXRob24gMyAoaXB5a2VybmVsKSIsCiAgICJsYW5ndWFnZSI6ICJweXRob24iLAogICAibmFtZSI6ICJweXRob24zIgogIH0sCiAgImxhbmd1YWdlX2luZm8iOiB7CiAgICJjb2RlbWlycm9yX21vZGUiOiB7CiAgICAibmFtZSI6ICJpcHl0aG9uIiwKICAgICJ2ZXJzaW9uIjogMwogICB9LAogICAiZmlsZV9leHRlbnNpb24iOiAiLnB5IiwKICAgIm1pbWV0eXBlIjogInRleHQveC1weXRob24iLAogICAibmFtZSI6ICJweXRob24iLAogICAibmJjb252ZXJ0X2V4cG9ydGVyIjogInB5dGhvbiIsCiAgICJweWdtZW50c19sZXhlciI6ICJpcHl0aG9uMyIsCiAgICJ2ZXJzaW9uIjogIjMuMTEuNyIKICB9LAogICJ3aWRnZXRzIjogewogICAiYXBwbGljYXRpb24vdm5kLmp1cHl0ZXIud2lkZ2V0LXN0YXRlK2pzb24iOiB7CiAgICAic3RhdGUiOiB7fSwKICAgICJ2ZXJzaW9uX21ham9yIjogMiwKICAgICJ2ZXJzaW9uX21pbm9yIjogMAogICB9CiAgfQogfSwKICJuYmZvcm1hdCI6IDQsCiAibmJmb3JtYXRfbWlub3IiOiA1Cn0K
""".strip()
# PYTHON_TEMPLATE_START

# DENO_TEMPLATE_START
# 2024-02-11T18:07:50-08:00
TEMPLATES[
    "deno"
] = """
ewogImNlbGxzIjogWwogIHsKICAgImNlbGxfdHlwZSI6ICJtYXJrZG93biIsCiAgICJpZCI6ICI2ZmY4MDczNC04OTA2LTRmODUtOWFhYi02Y2VhY2U3YmE0MjUiLAogICAibWV0YWRhdGEiOiB7CiAgICAiZWRpdGFibGUiOiB0cnVlLAogICAgInNsaWRlc2hvdyI6IHsKICAgICAic2xpZGVfdHlwZSI6ICIiCiAgICB9LAogICAgInRhZ3MiOiBbXQogICB9LAogICAic291cmNlIjogWwogICAgIiMgVElUTEVcbiIsCiAgICAiIyMgREVTQ1JJUFRJT04iCiAgIF0KICB9LAogIHsKICAgImNlbGxfdHlwZSI6ICJtYXJrZG93biIsCiAgICJpZCI6ICIwNWIzZTg4MC04NjAxLTQxMDctOTg5NS1kNzkyYmExZGNkMzAiLAogICAibWV0YWRhdGEiOiB7CiAgICAiZWRpdGFibGUiOiB0cnVlLAogICAgInNsaWRlc2hvdyI6IHsKICAgICAic2xpZGVfdHlwZSI6ICIiCiAgICB9LAogICAgInRhZ3MiOiBbXQogICB9LAogICAic291cmNlIjogWwogICAgIiMjIFNldHVwIgogICBdCiAgfSwKICB7CiAgICJjZWxsX3R5cGUiOiAiY29kZSIsCiAgICJleGVjdXRpb25fY291bnQiOiBudWxsLAogICAiaWQiOiAiMTE3MzA3ZTQtZTY2Zi00MDQ0LWI3ZTctOTE0ZGMwMjkyODIxIiwKICAgIm1ldGFkYXRhIjogewogICAgInRhZ3MiOiBbCiAgICAgInBhcmFtZXRlcnMiCiAgICBdCiAgIH0sCiAgICJvdXRwdXRzIjogW10sCiAgICJzb3VyY2UiOiBbCiAgICAiLy8gRGVmYXVsdCBQYXJhbXNcbiIsCiAgICAidmFyIHNlcnZlciA9IFwibWFpbi54YXJncy5pb1wiIgogICBdCiAgfSwKICB7CiAgICJjZWxsX3R5cGUiOiAiY29kZSIsCiAgICJleGVjdXRpb25fY291bnQiOiBudWxsLAogICAiaWQiOiAiNGIzMDU4ZGEiLAogICAibWV0YWRhdGEiOiB7CiAgICAidGFncyI6IFtdCiAgIH0sCiAgICJvdXRwdXRzIjogW10sCiAgICJzb3VyY2UiOiBbCiAgICAiaW1wb3J0IHtzaCwgJH0gZnJvbSAnaHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL3pwaC9ydW5ib29rL21haW4vZXh0L2Rlbm8tcnVuYm9vay9tb2QudHMnIgogICBdCiAgfSwKICB7CiAgICJjZWxsX3R5cGUiOiAiY29kZSIsCiAgICJleGVjdXRpb25fY291bnQiOiBudWxsLAogICAiaWQiOiAiYjI3ZGVmNTYtMDIxOS00Mzg5LTgyYzctNDRjNzdiYWI2YjE5IiwKICAgIm1ldGFkYXRhIjogewogICAgInRhZ3MiOiBbXQogICB9LAogICAib3V0cHV0cyI6IFtdLAogICAic291cmNlIjogWwogICAgImF3YWl0IHNoKFwiZ2l0IGxvZ1wiKSIKICAgXQogIH0sCiAgewogICAiY2VsbF90eXBlIjogIm1hcmtkb3duIiwKICAgImlkIjogImI3ZjE1MDk4LWQ1NDAtNGMyNC04M2JjLTczZjhiODE2ODhjNyIsCiAgICJtZXRhZGF0YSI6IHsKICAgICJlZGl0YWJsZSI6IHRydWUsCiAgICAic2xpZGVzaG93IjogewogICAgICJzbGlkZV90eXBlIjogIiIKICAgIH0sCiAgICAidGFncyI6IFtdCiAgIH0sCiAgICJzb3VyY2UiOiBbCiAgICAiIyMgT3BlcmF0aW9uIgogICBdCiAgfSwKICB7CiAgICJjZWxsX3R5cGUiOiAibWFya2Rvd24iLAogICAiaWQiOiAiYTVmODVkZGQtNjVlOC00ZDA0LTk2OTItZTUwNzI0ZjNhNjk3IiwKICAgIm1ldGFkYXRhIjogewogICAgImVkaXRhYmxlIjogdHJ1ZSwKICAgICJzbGlkZXNob3ciOiB7CiAgICAgInNsaWRlX3R5cGUiOiAiIgogICAgfSwKICAgICJ0YWdzIjogW10KICAgfSwKICAgInNvdXJjZSI6IFsKICAgICIjIyMgU3RlcCAxLiBFY2hvIEpTT04iCiAgIF0KICB9LAogIHsKICAgImNlbGxfdHlwZSI6ICJjb2RlIiwKICAgImV4ZWN1dGlvbl9jb3VudCI6IG51bGwsCiAgICJpZCI6ICJlNzc0ZTdjYSIsCiAgICJtZXRhZGF0YSI6IHsKICAgICJ0YWdzIjogW10KICAgfSwKICAgIm91dHB1dHMiOiBbXSwKICAgInNvdXJjZSI6IFsKICAgICJhd2FpdCAkYGVjaG8gJ3tcImFcIjogMX0nYC5qc29uKCkiCiAgIF0KICB9LAogIHsKICAgImNlbGxfdHlwZSI6ICJtYXJrZG93biIsCiAgICJpZCI6ICJjOTdhMzIxZS1kYmU3LTRlZGEtOTI5Yi04N2ZjNmFhMjkwNTIiLAogICAibWV0YWRhdGEiOiB7CiAgICAiZWRpdGFibGUiOiB0cnVlLAogICAgInNsaWRlc2hvdyI6IHsKICAgICAic2xpZGVfdHlwZSI6ICIiCiAgICB9LAogICAgInRhZ3MiOiBbXQogICB9LAogICAic291cmNlIjogWwogICAgIiMjIyBTdGVwIDIgR2V0IEdpdCBMb2ciCiAgIF0KICB9LAogIHsKICAgImNlbGxfdHlwZSI6ICJjb2RlIiwKICAgImV4ZWN1dGlvbl9jb3VudCI6IG51bGwsCiAgICJpZCI6ICI2ZWVkNmU0NiIsCiAgICJtZXRhZGF0YSI6IHsKICAgICJ0YWdzIjogW10KICAgfSwKICAgIm91dHB1dHMiOiBbXSwKICAgInNvdXJjZSI6IFsKICAgICJhd2FpdCAkYGdpdCBsb2dgLnRleHQoKSIKICAgXQogIH0sCiAgewogICAiY2VsbF90eXBlIjogIm1hcmtkb3duIiwKICAgImlkIjogImVjYTMwZGUwLWJhNjUtNDNjNi1iMjIwLWNhYjBkYWUzNjNmZiIsCiAgICJtZXRhZGF0YSI6IHsKICAgICJlZGl0YWJsZSI6IHRydWUsCiAgICAic2xpZGVzaG93IjogewogICAgICJzbGlkZV90eXBlIjogIiIKICAgIH0sCiAgICAidGFncyI6IFtdCiAgIH0sCiAgICJzb3VyY2UiOiBbCiAgICAiIyMgUm9sbGJhY2siCiAgIF0KICB9LAogIHsKICAgImNlbGxfdHlwZSI6ICJtYXJrZG93biIsCiAgICJpZCI6ICJmY2UwODQwNC00ZWIxLTQ1ZDMtOGY5Yy0yZTU2MDE2NjI5NjIiLAogICAibWV0YWRhdGEiOiB7CiAgICAiZWRpdGFibGUiOiB0cnVlLAogICAgInNsaWRlc2hvdyI6IHsKICAgICAic2xpZGVfdHlwZSI6ICIiCiAgICB9LAogICAgInRhZ3MiOiBbXQogICB9LAogICAic291cmNlIjogWwogICAgIiMjIENsZWFudXAiCiAgIF0KICB9LAogIHsKICAgImNlbGxfdHlwZSI6ICJtYXJrZG93biIsCiAgICJpZCI6ICIzNmNmZTQ2Mi1lNDI0LTQ1OWItOTU3YS0wZTA2ZDIzMWM5MjgiLAogICAibWV0YWRhdGEiOiB7CiAgICAiZWRpdGFibGUiOiB0cnVlLAogICAgInNsaWRlc2hvdyI6IHsKICAgICAic2xpZGVfdHlwZSI6ICIiCiAgICB9LAogICAgInRhZ3MiOiBbXQogICB9LAogICAic291cmNlIjogWwogICAgIiMjIEFjdGlvbiBJdGVtcyAvIExlYXJuaW5ncyIKICAgXQogIH0KIF0sCiAibWV0YWRhdGEiOiB7CiAgImtlcm5lbHNwZWMiOiB7CiAgICJkaXNwbGF5X25hbWUiOiAiRGVubyIsCiAgICJsYW5ndWFnZSI6ICJ0eXBlc2NyaXB0IiwKICAgIm5hbWUiOiAiZGVubyIKICB9LAogICJsYW5ndWFnZV9pbmZvIjogewogICAiZmlsZV9leHRlbnNpb24iOiAiLnRzIiwKICAgIm1pbWV0eXBlIjogInRleHQveC50eXBlc2NyaXB0IiwKICAgIm5hbWUiOiAidHlwZXNjcmlwdCIsCiAgICJuYl9jb252ZXJ0ZXIiOiAic2NyaXB0IiwKICAgInB5Z21lbnRzX2xleGVyIjogInR5cGVzY3JpcHQiLAogICAidmVyc2lvbiI6ICI1LjMuMyIKICB9LAogICJ3aWRnZXRzIjogewogICAiYXBwbGljYXRpb24vdm5kLmp1cHl0ZXIud2lkZ2V0LXN0YXRlK2pzb24iOiB7CiAgICAic3RhdGUiOiB7fSwKICAgICJ2ZXJzaW9uX21ham9yIjogMiwKICAgICJ2ZXJzaW9uX21pbm9yIjogMAogICB9CiAgfQogfSwKICJuYmZvcm1hdCI6IDQsCiAibmJmb3JtYXRfbWlub3IiOiA1Cn0K
""".strip()
# DENO_TEMPLATE_START
