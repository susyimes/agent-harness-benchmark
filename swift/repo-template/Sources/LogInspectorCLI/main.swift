import Foundation
import LogInspector

let args = CommandLine.arguments
if args.count < 4 || args[1] != "search" {
    fputs("usage: loginspect search <file> <keyword>\n", stderr)
    exit(1)
}
let file = args[2]
let keyword = args[3]
let parser = LogParser()
let engine = SearchEngine()
let text = try String(contentsOfFile: file, encoding: .utf8)
let entries = try text.split(separator: "\n").map { try parser.parse(String($0)) }
let result = engine.search(entries, keyword: keyword, caseSensitive: false)
for item in result {
    print("\(item.timestamp) [\(item.level)] \(item.message)")
}
