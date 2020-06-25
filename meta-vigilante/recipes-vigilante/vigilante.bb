
LICENSE ="CLOSED"

SRC_URI = "file://deep_learning_object_detection.py \
	   file://MobileNetSSD_deploy.caffemodel \
	   file://MobileNetSSD_deploy.prototxt.txt \
	   file://paths.py \
	   file://registro.txt \
	   file://view.py"

S = "${WORKDIR}"



do_install() {
    install -d ${D}${base_bindir}/vigilante
    install -d ${D}${base_bindir}/vigilante/Remoto
    install -d ${D}${base_bindir}/vigilante/Avistamientos
    install -m 0755 deep_learning_object_detection.py ${D}${base_bindir}/vigilante
    install -m 0755 MobileNetSSD_deploy.caffemodel ${D}${base_bindir}/vigilante
    install -m 0755 MobileNetSSD_deploy.prototxt.txt ${D}${base_bindir}/vigilante
    install -m 0755 paths.py ${D}${base_bindir}/vigilante
    install -m 0755 registro.txt ${D}${base_bindir}/vigilante
    install -m 0755 view.py ${D}${base_bindir}/vigilante
}


