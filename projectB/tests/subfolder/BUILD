package(default_visibility = ["//visibility:public"])

load("@my_deps//:requirements.bzl", "requirement")

py_test(
	name = "test_bar2_subfolder",
	srcs = ["test_bar2_subfolder.py"],
	deps = [
		"//projectB/src:bar2",
		requirement("xmlrunner"),
	]
)