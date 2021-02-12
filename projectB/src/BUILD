package(default_visibility = ["//visibility:public"])

load("@my_deps//:requirements.bzl", "requirement")

py_library(
    name = "__init__",
    srcs = ["__init__.py"],
    deps = ["//projectB/src:bar1"],
)

py_binary(
    name = "bar1",
    srcs = ["bar1.py"],
    deps = [requirement("numpy")],
)

py_binary(
    name = "bar2",
    srcs = ["bar2.py"],
    deps = [
        "//projectB/src:bar1",
        requirement("pyyaml"),
    ],
)

py_binary(
	name = "sample",
	srcs = ["sample.py"],
	deps = [
		"//projectB/src:bar2"
	]
)