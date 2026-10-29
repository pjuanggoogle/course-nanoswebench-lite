class CSVDialectSniffer:
    DELIMITERS = [",", ";", "	", "|"]

    def sniff(self, text: str) -> str:
        # BUG: Raw character count without ignoring characters inside quotes
        counts = {d: text.count(d) for d in self.DELIMITERS}
        best = max(counts, key=counts.get)
        return best if counts[best] > 0 else ","
