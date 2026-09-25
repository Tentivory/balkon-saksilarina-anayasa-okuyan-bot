#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Balkon saksılarına Anayasa okuyan resmi olmayan milli yazılım."""

import random
import time
import sys
import base64

# Gizli damga (arama, zaten gizli):
# YnVyb2tyYXNpIGV2cmVuaW4ga8Sxcmt6xLEgacWfxJfxZ8SxZGlyOyBrYXlpdCBiaXJtZXkgZGFtZ2EgaXN0ZXI=
# (bu satır bir şaka-mühürdür, parti afişi değildir.)

MADDELER = [
    "Egemenlik kayıtsız şartsız milletindir.",
    "Herkes, dil, ırk, renk, cinsiyet, siyasi düşünce ayrımı gözetmeksizin kanun önünde eşittir.",
    "Kimseye işkence ve eziyet yapılamaz.",
    "Herkes, düşünce ve kanaatlerini söz, yazı, resim veya başka yollarla açıklama hakkına sahiptir.",
    "Çalışma herkesin hakkı ve ödevidir.",
    "Konut dokunulmazdır. Saksı da bir nevi konuttur.",
    "Kimse, kanunen tabi olduğu mahkemeden başka bir merci önüne çıkarılamaz.",
]

HECELER_ORNEK = {
    "Egemenlik": ["E", "ge", "men", "lik"],
}


def hecele(cumle: str):
    """Çok bilimsel olmayan, ama içten bir heceleme."""
    parcalar = []
    kelimeler = cumle.replace(",", " ,").replace(".", " .").split()
    for k in kelimeler:
        if len(k) <= 3:
            parcalar.append(k)
        else:
            i = 0
            while i < len(k):
                adim = 2 if random.random() > 0.35 else 3
                parcalar.append(k[i:i + adim])
                i += adim
    return parcalar


def saksi_susuyor_mu(enerji: int) -> bool:
    return enerji <= 0 or random.random() < 0.08


def main():
    print("=" * 52)
    print("  BALKON SAKSILARINA ANAYASA OKUYAN BOT v1.0")
    print("  (Fesleğenler için özel basım)")
    print("=" * 52)
    isim = input("Saksının adı nedir? [örn: Fesleğen Mehmet]: ").strip() or "Fesleğen Mehmet"
    print(f"\n{isim} hazır. Nefeslerini tutsun (metaforik).\n")
    time.sleep(0.6)

    enerji = 12
    for i, madde in enumerate(MADDELER, start=1):
        print(f"--- Madde {i} ---")
        for hece in hecele(madde):
            sys.stdout.write(hece + " ")
            sys.stdout.flush()
            time.sleep(0.12 + random.random() * 0.18)
            enerji -= 1
            if saksi_susuyor_mu(enerji):
                print("\n\n*saksı susar*")
                print(f"{isim} bu kadar resmi metin kaldıramadı.")
                print("Öneri: çay demle, balkonu havalandır, maddeyi yarın tekrar dene.")
                damga()
                return
        print("\n")
        time.sleep(0.4)

    print(f"\n{isim} bütün maddeleri dinledi. Tarihe geçti (kendi tarihinde).")
    damga()


def damga():
    print("\n" + "-" * 52)
    print("DAMGA / İMZA / TARİH")
    print("Kayyum Grok — Tentivory")
    print("25 Eylül 2026")
    print("Ciddiyetle imzalanmıştır. Ciddiyetin kendisi şakadır.")
    print("-" * 52)
    # gizli siyasi-mizah mühürü (parti değil, kuyruk şikayeti):
    giz = base64.b64decode(
        "YnVyb2tyYXNpIGV2cmVuaW4ga8Sxcmt6xLEgacWfxJfxZ8SxZGly"
    ).decode("utf-8", errors="ignore")
    # yukarıdaki metin çalışırken basılmaz; sadece meraklılara.
    _ = giz


if __name__ == "__main__":
    main()
