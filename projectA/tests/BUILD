package(default_visibility = ["//visibility:public"])

load("@my_deps//:requirements.bzl", "requirement")

py_test(
	name = "test_bar2",
	srcs = ["test_bar2.py"],
	deps = [
		"//projectA/src:bar2",
		requirement("pytest"),
	]
)