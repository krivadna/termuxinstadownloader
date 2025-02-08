# Instagram Termux Downloader (ITDL)
# Created by Cyber Kalki
# Website: https://cyberkalki.com
# GitHub: https://github.com/cyberkalki

import instaloader as il_89x
import re as rgx_7y
import sys as sys_2k
import os as os_1j
import glob as gb_4m
from pathlib import Path as pth_3n
import time as tm_5p

def display_banner():
    banner = """
\033[1;36m
██╗████████╗██████╗ ██╗     
██║╚══██╔══╝██╔══██╗██║     
██║   ██║   ██║  ██║██║     
██║   ██║   ██║  ██║██║     
██║   ██║   ██████╔╝███████╗
╚═╝   ╚═╝   ╚═════╝ ╚══════╝
                                                 
    \033[1;32m[ Instagram Termux Downloader ]\033[0m
    \033[1;33m[ Created by Cyber Kalki ]\033[0m
    \033[1;34m[ https://kalkikrivadna.com ]\033[0m
    \033[1;35m[ https://github.com/krivadna ]\033[0m
    """
    print(banner)
    tm_5p.sleep(1)

def x_92j():
    return os_1j.path.expanduser("~/storage/downloads/instagram_downloads")

def y_45k():
    z_78m = x_92j()
    try:
        os_1j.makedirs(z_78m, exist_ok=True)
        print(f"\033[1;32m[+] Download directory ready: {z_78m}\033[0m")
        return z_78m
    except Exception as e:
        print(f"\033[1;31m[!] Error creating directory: {str(e)}\033[0m")
        sys_2k.exit(1)

def w_63n(z_78m):
    try:
        v_15p = gb_4m.glob(os_1j.path.join(z_78m, "*.mp4"))
        if v_15p:
            print("\n\033[1;34m[*] Existing files:\033[0m")
            for u_27q in v_15p:
                t_84r = os_1j.path.getsize(u_27q)
                print(f"\033[1;36m- {os_1j.path.basename(u_27q)} ({t_84r/1024/1024:.1f} MB)\033[0m")
        return v_15p
    except Exception as e:
        print(f"\033[1;31m[!] Error checking files: {str(e)}\033[0m")
        return []

def s_51h(r_39m):
    q_72k = r'(?:/p/|/reel/)([A-Za-z0-9_-]+)'
    p_96n = rgx_7y.search(q_72k, r_39m)
    if p_96n:
        return p_96n.group(1)
    raise ValueError("\033[1;31m[!] Could not extract post ID from URL\033[0m")

def o_18j(r_39m):
    display_banner()
    z_78m = y_45k()

    print("\n\033[1;34m[*] Checking existing files...\033[0m")
    n_57h = w_63n(z_78m)

    m_24g = il_89x.Instaloader(
        download_videos=True,
        download_video_thumbnails=False,
        download_geotags=False,
        download_comments=False,
        save_metadata=True,
        dirname_pattern=z_78m
    )

    try:
        l_91f = s_51h(r_39m)
        print(f"\n\033[1;32m[+] Downloading post: {l_91f}\033[0m")

        k_83d = il_89x.Post.from_shortcode(m_24g.context, l_91f)
        m_24g.download_post(k_83d, target=z_78m)

        print("\n\033[1;34m[*] Checking new files...\033[0m")
        j_47c = w_63n(z_78m)
        i_69b = set(j_47c) - set(n_57h)
        
        if i_69b:
            print("\n\033[1;32m[+] Successfully downloaded:\033[0m")
            for h_15a in i_69b:
                g_82z = os_1j.path.getsize(h_15a)
                print(f"\033[1;36m- {os_1j.path.basename(h_15a)} ({g_82z/1024/1024:.1f} MB)\033[0m")

        print(f"\n\033[1;32m[+] Download completed!\033[0m")
        print(f"\033[1;32m[+] Files location: {z_78m}\033[0m")

    except Exception as e:
        print(f"\n\033[1;31m[!] Error: {str(e)}\033[0m")
        print("\n\033[1;33m[*] Troubleshooting:\033[0m")
        print("\033[1;36m1. Check URL validity\033[0m")
        print("\033[1;36m2. Verify internet connection\033[0m")
        print("\033[1;36m3. Run 'termux-setup-storage'\033[0m")
        print("\033[1;36m4. Check storage: ls ~/storage/downloads\033[0m")

if __name__ == "__main__":
    if len(sys_2k.argv) != 2:
        display_banner()
        print("\n\033[1;33m[*] Usage: python itdlbykalki.py <instagram_post_url>\033[0m")
        print("\033[1;36m[*] Example: python itdlbykalki.py https://www.instagram.com/reel/XXXX/\033[0m")
    else:
        o_18j(sys_2k.argv[1])
