from collections import defaultdict
import concurrent.futures

from flask import Blueprint, request
import logging

from classnamer_reader import ClassNamerReader

routes = Blueprint(__name__, 'blueprint')


@routes.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    header['Access-Control-Allow-Method'] = 'GET'
    header['Access-Control-Allow-Headers'] = 'Origin, Content-Type, X-Auth-Token'
    return response


@routes.route('/classNames', methods=['GET'])
def get_class_names():
    logging.info("Get classNames")
    all_class_names = defaultdict(int)

    def add_class_name():
        class_namer_words = ClassNamerReader(url="https://www.classnamer.org").extract()
        for word in class_namer_words:
            all_class_names[word] = all_class_names[word] + 1
        return all_class_names

    amount = int(request.args.get("amount", 100))
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        for i in range(0, amount):
            executor.submit(add_class_name)
    return all_class_names, 200
