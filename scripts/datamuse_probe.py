#!/usr/bin/env python3
"""Fetch pun-construction raw material from Datamuse and icanhazdadjoke.

Example:
    python3 scripts/datamuse_probe.py \
      --topic "marketing and AI" \
      --handle marketing --handle ai --handle funnel --handle model --expand
"""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import sys
import urllib.parse
import urllib.request


def fetch_json(url: str, headers: dict[str, str] | None = None):
    try:
        req = urllib.request.Request(url)
        for key, value in (headers or {}).items():
            req.add_header(key, value)
        with urllib.request.urlopen(req, timeout=8) as response:
            return json.loads(response.read())
    except Exception:
        return None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fetch sound-alikes, homophones, and optional semantic expansions for pun handles."
    )
    parser.add_argument("--topic", default="", help="Topic for seed joke lookup.")
    parser.add_argument(
        "--handle",
        action="append",
        dest="handles",
        default=[],
        help="Handle to probe. Repeat for multiple handles.",
    )
    parser.add_argument(
        "--skip-seeds",
        action="store_true",
        help="Skip icanhazdadjoke lookup. Useful for random mode.",
    )
    parser.add_argument(
        "--expand",
        action="store_true",
        help="Also fetch Datamuse means-like terms for each handle.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    handles = [handle.strip() for handle in args.handles if handle and handle.strip()]
    if not handles:
        print("Error: provide at least one --handle", file=sys.stderr)
        return 1

    jobs: dict[str, tuple[str, dict[str, str] | None]] = {}

    if args.topic and not args.skip_seeds:
        topic = urllib.parse.quote(args.topic)
        jobs["seeds"] = (
            f"https://icanhazdadjoke.com/search?term={topic}&limit=3",
            {"Accept": "application/json"},
        )

    for handle in handles:
        quoted = urllib.parse.quote(handle)
        jobs[f"sl:{handle}"] = (f"https://api.datamuse.com/words?sl={quoted}&max=8", None)
        jobs[f"hom:{handle}"] = (f"https://api.datamuse.com/words?rel_hom={quoted}&max=5", None)
        if args.expand:
            jobs[f"ml:{handle}"] = (f"https://api.datamuse.com/words?ml={quoted}&max=8", None)

    results: dict[str, object] = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=min(32, len(jobs) or 1)) as pool:
        future_map = {
            pool.submit(fetch_json, url, headers): key
            for key, (url, headers) in jobs.items()
        }
        for future in concurrent.futures.as_completed(future_map):
            results[future_map[future]] = future.result()

    print("SEED JOKES:")
    seed_data = results.get("seeds")
    if isinstance(seed_data, dict) and seed_data.get("results"):
        for joke in seed_data["results"][:3]:
            print(f"- {joke.get('joke', '')}")
    else:
        print("- (none)")

    print()
    print("SOUND-ALIKE PAIRS:")
    for handle in handles:
        sound_data = results.get(f"sl:{handle}")
        if isinstance(sound_data, list):
            words = [item["word"] for item in sound_data if item.get("word") != handle][:6]
            print(f"- {handle} -> {', '.join(words) if words else '(none)'}")

    print()
    print("HOMOPHONES:")
    for handle in handles:
        homophone_data = results.get(f"hom:{handle}")
        if isinstance(homophone_data, list):
            words = [item["word"] for item in homophone_data if item.get("word")]
            print(f"- {handle} -> {', '.join(words) if words else '(none)'}")

    if args.expand:
        print()
        print("MEANS-LIKE:")
        for handle in handles:
            expansion_data = results.get(f"ml:{handle}")
            if isinstance(expansion_data, list):
                words = [item["word"] for item in expansion_data if item.get("word")][:8]
                print(f"- {handle} -> {', '.join(words) if words else '(none)'}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
