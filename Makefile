IMAGE_VERSION ?= v3.0
IMG ?= registry.app.dev.gembotech.cn/example/hello:$(IMAGE_VERSION)

BUILDAH_FORMAT ?= docker

all:
	docker build -t $(IMG) .
	docker push $(IMG)
