import scrapy


class DevV1Spider(scrapy.Spider):
    name = "dev_v1"
    # allowed_domains = ["x"]
    # start_urls = ["https://x"]

    url = 'https://shopee.com.my/api/v4/search/search_items?by=sales&limit=60&match_id=11000710&newest=0&order=desc&page_type=search&scenario=PAGE_CATEGORY&version=2&view_session_id=78e7ed9e-a6d4-4de1-ac96-ba4e65aca869'

    headers = {
        "5a7ca7a": "afrom scrapy import Request url = 'https://shopee.com.my/api/v4/search/search_items?by=sales&limit=60&match_id=11000710&newest=0&order=desc&page_type=search&scenario=PAGE_CATEGORY&version=2&view_session_id=78e7ed9e-a6d4-4de1-ac96-ba4e65aca869' headers = s88O/-^?hS1X\\:/EIYqMAf",
            "6280f0e2": "84JAd;^+HZQV\\5%lG<8>m\"7k]",
            "authority": "shopee.com.my",
            "accept": "application/json",
            "accept-language": "en-US,en;q=0.9,ms;q=0.8,id;q=0.7",
            "af-ac-enc-dat": "AAcyLjguMS0yAAABiFHZ/qgAABDwAzAAAAAAAAAAAlkZhtdckEfTGjjUaOpynQIB1hHv+IodUHfZOTJTf8q/bLui+q/hrS2PdTmSh5YHOYKH/j73yNn/3TW2ljCJhOMYX/bENnAJuNoEC605xFT503Yv+A9QKLE/lVNOHvHwvRDXMpFXlNgyym91W9+wJ5Hh2biXMwCjqYicEjEeh8/ZW8DGKtEW/Xk5hCkhd/3pjmeBy380vQIGd21h2hqbVNQIebNX3Mpmcx+WlQrp3VazrDwPTHH6y6ljQXSA41rvHaJyWfJEge6Tmo9pBgx3W6SfOAKFLPhCw4F5DkYfoMMAf9m8eKbyhn5a5BNrE/s8kG1RE6iiXcTXwvvlmBo3CtEJKmpDRWWmkzhGMazGdbRC/ZIKLZf/NhMnw8f21UXD2mkb2JuX/zYTJ8PH9tVFw9ppG9ibP/BOz2oYo04ucXv4uBSZr/mBzz7CMldMFN7MtoLQaiGjwU40zulgBLQEfvh0NyLYWtjMbUo+dtE8b938TVtvMRgJlH0Uh7askuCBS5FqVhjc7PsqCeEaqZ+HwwkZhQXXNvXIna4MPofS8Zscif6cv0k73cIa1gyb5TjRdOHMVOPKVqj/obTSEr2OBklism5ip7xsBGDruke61bCKTKdeh/fI2f/dNbaWMImE4xhf9sT4nXr/+i8dLKiDLBIGP692bDthdB1Do2VebT5xZOmCjvXnb2wb1IJa7OCghYt6KLa2Rmv8pCPiEApmEAaeHiqjB/0EnmuaXM8yBzVUNBzbPprROMJkcN15n4kILPQyPRq0AntGfasU53wS90KRUkfUQgFqSO+Kjkx02Jlm8cFNXuw4XwlboXSrhzYEylKOuxoKWrOnq6+YUWe5XcPDKt+KQgFqSO+Kjkx02Jlm8cFNXqKSaxyyekOJL+c7ULfKHELahYF5hK6+uNPPhgQOU/pYy8W6LkL4KiSFzjuz0gQUiwYNS2kSk1JIjSg63e1qA5O20y7c/eq7SlPBfkItD4rubE8OphWhMES3ji7wSLmvMgYNS2kSk1JIjSg63e1qA5OX+yIurpSBgrqEApRZVYT8l/82EyfDx/bVRcPaaRvYmwJtdp774yFFyjUxWfYWHWM=",
            "af-ac-enc-sz-token": "txBYVg/clPP0amurypOoZQ==|ZClVIUGeTtVEL7azT/eqYD9mxOCLVnBBnRVKLP/30aVVqYbsx2YSBS6LxQ5KNqzrUvT4QlQ8C5xuovK+k6tgQStrnHQZWvHAeQ==|tHGDi8LyEF+sefTT|06|3",
            "content-type": "application/json",
            "dnt": "1",
            "sec-ch-ua": "\"Microsoft Edge\";v=\"113\", \"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Linux\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "sz-token": "txBYVg/clPP0amurypOoZQ==|ZClVIUGeTtVEL7azT/eqYD9mxOCLVnBBnRVKLP/30aVVqYbsx2YSBS6LxQ5KNqzrUvT4QlQ8C5xuovK+k6tgQStrnHQZWvHAeQ==|tHGDi8LyEF+sefTT|06|3",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50",
            "x-api-source": "pc",
            "x-csrftoken": "jQBY0wYg7nzVzhRSfe5UrQgdhcq39stw",
            "x-requested-with": "XMLHttpRequest",
            "x-sap-access-f": "3.2.113.4.0|13|2.8.1-2_5.5.71_0_158|9989724098dc4b8aa736e53a07a544cd0bcee834282648|10900|100",
            "x-sap-access-s": "HWyfzt7X2YYv3depaO-gZs22jYOg2XNlk9aZFEBrmB8=",
            "x-sap-access-t": "1685009430",
            "x-sap-ri": "2b346f64e78a25ec49a38b30f91095136078bd9ab6fd0eb6",
            "x-shopee-language": "en",
            "x-sz-sdk-version": "2.8.1-2@1.2.1"
        }

    cookies = {
        "__LOCALE__null": "MY",
        "SPC_SI": "z2VsZAAAAAB4TThYakNFNVngHwAAAAAAd2VDZGpoVUg=",
        "SPC_F": "nA5PLenPPVVk7kisMl86LiDFxLw31d72",
        "REC_T_ID": "2fa488f7-fa96-11ed-83e7-08f1ea7c65fc",
        "csrftoken": "jQBY0wYg7nzVzhRSfe5UrQgdhcq39stw",
        "language": "en",
        "SPC_CLIENTID": "bkE1UExlblBQVlZrgginfbwebfoonwot",
        "SPC_P_V": "0ZkyBiKjMhnlxhKV/gOgnAyu8K+py2DkX8sd7izSFqBbl0h+qi5svkE2jXtsijja/IOwexr5kND6RkQHaCMyxO6D4ItLsCuBnOJsraO/DFdD1TognjXIK7W61yyneF43bim8bleTCGgVCh0Ogj99gkTMkdN1cM82PhrAVy7uNPo=",
        "SPC_ST": ".aFFNQjF1QmhScTlyY1JscTE2LwjxTYh2YQTIrreI56QaoqbgkJBb3HNpx965VKX0PR4s13KZNAY9g6GEkAp14taNlNWLpT8kC3YwZmNGJ1HBa5446aVM7iGyX8Ub2QZ4ERNyzP+k6Rw5ClPQax4JjsFIAUU6tfgRxOpGwmDKYo5i/Mrn5OWNtG1P+Pxw40whxKWdVFIF1yEHauYxdVGW0A==",
        "SPC_U": "1005828798",
        "SPC_R_T_ID": "6lTHxR9S8/6eOxHbvDkLu18PRM8qYvDQRwlJQoJcVf3WPz5DyB/s8m/E36w7NY7dF/pZrQ+VjdVqmhOxG8ClHXa75CBBFHb/BlUniZRLWOXc9Aadf+lX+pTeIHKrRWeA9BI5CxATenZvQeqRFmxdOX2e0RMj9gI0i3M8Ok3QPPQ=",
        "SPC_R_T_IV": "Y3Fsc1NZTWtnaE1CUUtVSg==",
        "SPC_T_ID": "6lTHxR9S8/6eOxHbvDkLu18PRM8qYvDQRwlJQoJcVf3WPz5DyB/s8m/E36w7NY7dF/pZrQ+VjdVqmhOxG8ClHXa75CBBFHb/BlUniZRLWOXc9Aadf+lX+pTeIHKrRWeA9BI5CxATenZvQeqRFmxdOX2e0RMj9gI0i3M8Ok3QPPQ=",
        "SPC_T_IV": "Y3Fsc1NZTWtnaE1CUUtVSg==",
        "shopee_webUnique_ccd": "UMukUzT5qbbyJwYco3Do%2BQ%3D%3D%7CaylVIUGeTtVEL7azT%2FeqYD9mxOCLVnBBnRVKLP%2F30aVVqYbsx2YSBS6LxQ5KNqzrUvT4QlQ8C5xuovK%2Bk6tgQStrlnwZWvHAeQ%3D%3D%7CtHGDi8LyEF%2BsefTT%7C06%7C3",
        "ds": "35fc8e666774c3071b37c0f63121fa5d",
        "SPC_EC": "ZVlNUkhBZ2FZOU9VTHg5S15Rt1NT0FwPOBQmWMPixJPJ11w1i+Lk0v0az6WsNevXC/PMWnnqg2vpTb1L/QLm02+Pa+VU7gTnHyuibS3kSgK4TzTvSdyUHT8R+cYwBjAivEbtxVtOPXB6r1FumPB0R6JxnTQPfX8zHIeSDNIuwDY="
    }

    def start_requests(self):
        ...

    def parse(self, response):
        pass
