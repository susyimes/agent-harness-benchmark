// swift-tools-version: 5.9
import PackageDescription

let package = Package(
    name: "SwiftLogInspectorBenchmark",
    platforms: [.macOS(.v13)],
    products: [
        .executable(name: "loginspect", targets: ["LogInspectorCLI"]),
        .library(name: "LogInspector", targets: ["LogInspector"])
    ],
    targets: [
        .target(name: "LogInspector"),
        .executableTarget(name: "LogInspectorCLI", dependencies: ["LogInspector"]),
        .testTarget(name: "LogInspectorTests", dependencies: ["LogInspector"])
    ]
)
