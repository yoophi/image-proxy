===========
Image Proxy
===========


.. image:: https://img.shields.io/pypi/v/image_proxy.svg
        :target: https://pypi.python.org/pypi/image_proxy

.. image:: https://img.shields.io/travis/yoophi/image_proxy.svg
        :target: https://travis-ci.com/yoophi/image_proxy

.. image:: https://readthedocs.org/projects/image-proxy/badge/?version=latest
        :target: https://image-proxy.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status




Simple WebService to proxy image urls


* Free software: MIT license
* Documentation: https://image-proxy.readthedocs.io.


Features
--------

* http://localhost:5000/img/http://some-host.com/some/image.jpg 

  http://some-host.com/some/image.jpg 를 가져와 캐시에 보관하고 출력합니다. 캐시에 보관되어 있는 경우, 캐시의 보관 내용을 출력합니다.

TODO
----

* redis 외의 캐시 지원.


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
