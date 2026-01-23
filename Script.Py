import requests
import json

cookies = {
    'JSESSIONID': 'F736DB5FD3CFA337328AEB208A806B66',
    '__session:sessionID:': 'https:',
    '__session:sessionID:htmlRevolving': 'DwGwlgBGAmC8BEAmAjAZgOwAZvwgYwHtoBTAZwV0JNIEkA7EgDwUAtFQC4TcRiA3YkAOQCuAWwTJKIAIaly8cKQAuACWKSSAJ3gA+YJIgALdcQBmFLe2AB6STsvgd4KHHgBhACwA2AJzoAgi+QAEUxAgCE3PwBWL283L1DfVAAxQORkHwBRD0oiMjFkbBx8XNoGYmZ4QHRlQBq5QCA9Th4+IVF4cXwpGQR5ZVUNbV0DI1N4bRraqxsre1BIGARIt2M8PAAORHQAWmJoaEiNtOIAIw2V5GgPDeNJZA9UYkwvFeNDw5zqBFQCwreyeiYEQBQcoB3W3qEC4vAEIjEEmksm6KjUxE0Oj0hhMZmB42stmmjjm8AWS1W6y2Oz2B2Op3Ol2ut3uj2er2K71aiEKmB+pX+8EAlJqAUltQeCmlDWjDOnIwIoEX0UYN0SMtPysZM7GAHLNnITlmtNttdvtkEcTmcLlcbncHk8XpyPqh2Zy-uUEIBNW0A+jaAQHcGhDmghEGK4ZKeojkQM0cNtG73RMcWqZk55ottSS9eTDZSTTTzfSrUyqHkCeyOczfmUKoBZxMAYXqCxqQlptPAdANS3pI-qooZmSvKmPq+MExPE3Vkg1Gqmm2kWhnW4uyVCRe0zx0VQDxnoAvvU9YJrPtF7VhXUD0tbsrDZjXUexU1jeM1A51pP1FON1LNdMtjJt8FQbgXea5TvggCR2oAvfobkKtbQru4rwi2IbtvK2jAeeKq4hqCZEneKYjumz4Ttm74zggbjft8i6lgggD+eoAOHKgVuIr1o2+7NsGbZyuGWhUUhPZxviWqDveqajhmL6TjmH4eGyJG-kuCCABiugDBATR3p0f6jFBjKoYdgq8mcZevY8beybDo+Y6Zq+U65iU8wSUUUlkfAgCssYAe7qKcKdYqRKTHqXBbFOTpqp6Te6GGQ+aZPuOWZvtOv6EfOkklNJ8DkYA-pGAFeBgDdNoAXMpeq5EENnuHlqUeGnwexqWZdGuncYFSZDiFgk4RF5kfmgP7xXZgDNNpULngTueVQQeMEsSeCqdX5KF9rxGFGaFJnCXhUWWfAnitdQCVAoA6srddu9H5dBzHHpp2gbWNV6of2QW1QJ2HhWZokEUt1lFrZ3KAGp2XXZT1O39Z5RXeWYb0nQFaE1fxWFhaZIn4dFSB2nFq12YAi3mAJn5Hofdt7l7V5rFmMjHoVf5VXA3xmHGUJuGRRZLKII9Dp2YAkCqAOnmW3KZBTaFbB2MKozgOE+dIMkzNZONXd0NuLDNlta9m1oyzfVs4eHPDdoL2bfj436RdoOkw1t1Q4tqAeCtJbcq6SXM25rOqQrQ2HVops89eRNTXV10Q-NlP5qgNOkSbgDzQebuUMQV1sHSVrr+2rp0TQZl1g7N5NNfdyCxRL8PcoAoYqAJkhgAnyulWWbkpFty1bg2h2xWe5+VF4E47fPE9N9U3ZDC1U18qfG-+gC98YAgdoB71QeY79nPaD3DtnZNwVXeDc0U2J4tPZL-6AErpQJ9198ul8VbEr2P0eawLjdu7P90eMR7d-hU3eAPCaecy0XA8DftW9mNfeeR0DdfO1P8fC3rLLIGfBead-yAEcdM2d9A67UfljJWWgwG7w1vzBursZ6J2hhgI2F8EAgOohA-uUCfqK1tjghB1V64u2ngnEWi1IhtyAR3CogBttUALu6a8MbQKHrAlhpCnaTzjkLXWLd8weDobTbkgBVNPAQXHK+DvrsxtiVSRPDP58O1k3d2YkU70KwfAQADaaADDXW+0jPrsMIQotiBi37V3VmQr+-CdbNw9rIBYmCEpJUAPOhRiwLo0tsHTef0FQeKschKOiDyHfwEY4j8kR55iP-IARLlpbGJ8cXPxT8AnaEScoiesc1FHzQYtNwoifb-nakk7xssH5mLLmYMp2SY5a0Fg4jR91TiuLsoATMzAD0dng9eJd0nDy0N09+vMcmNMPqg6hLI1jtO5IAZvtAAXqb00x8iakKkWSM2uYyD4oKoX-fM6BinPX-IAB+VAB+dss3xg8iElXOe-IAA',
    'regionCode': '',
    'regionFullName': '%E5%85%A8%E9%83%A8',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'es-US,es;q=0.9,es-419;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=utf-8',
    'Referer': 'https://www.plap.mil.cn/freecms-glht/site/juncai//cggg/index.html',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'nsssjss': 'O028FhntJEjC4y/MUVyLZt1TOnZ6qNLWjzwdKXzE7mxLNJsPbaeMwrz3qnAz/nb8y87iPsehsVy1zPqIjH9vNOVl67HTdFVulV7m0m35A5uAgZ027KzSTCdGTfAcC+x4rplp4LT0T/+Hm2vI1raKxHid+EAyA9TnLAnQbRAnA0k=',
    'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    # 'Cookie': 'JSESSIONID=F736DB5FD3CFA337328AEB208A806B66; __session:sessionID:=https:; __session:sessionID:htmlRevolving=DwGwlgBGAmC8BEAmAjAZgOwAZvwgYwHtoBTAZwV0JNIEkA7EgDwUAtFQC4TcRiA3YkAOQCuAWwTJKIAIaly8cKQAuACWKSSAJ3gA+YJIgALdcQBmFLe2AB6STsvgd4KHHgBhACwA2AJzoAgi+QAEUxAgCE3PwBWL283L1DfVAAxQORkHwBRD0oiMjFkbBx8XNoGYmZ4QHRlQBq5QCA9Th4+IVF4cXwpGQR5ZVUNbV0DI1N4bRraqxsre1BIGARIt2M8PAAORHQAWmJoaEiNtOIAIw2V5GgPDeNJZA9UYkwvFeNDw5zqBFQCwreyeiYEQBQcoB3W3qEC4vAEIjEEmksm6KjUxE0Oj0hhMZmB42stmmjjm8AWS1W6y2Oz2B2Op3Ol2ut3uj2er2K71aiEKmB+pX+8EAlJqAUltQeCmlDWjDOnIwIoEX0UYN0SMtPysZM7GAHLNnITlmtNttdvtkEcTmcLlcbncHk8XpyPqh2Zy-uUEIBNW0A+jaAQHcGhDmghEGK4ZKeojkQM0cNtG73RMcWqZk55ottSS9eTDZSTTTzfSrUyqHkCeyOczfmUKoBZxMAYXqCxqQlptPAdANS3pI-qooZmSvKmPq+MExPE3Vkg1Gqmm2kWhnW4uyVCRe0zx0VQDxnoAvvU9YJrPtF7VhXUD0tbsrDZjXUexU1jeM1A51pP1FON1LNdMtjJt8FQbgXea5TvggCR2oAvfobkKtbQru4rwi2IbtvK2jAeeKq4hqCZEneKYjumz4Ttm74zggbjft8i6lgggD+eoAOHKgVuIr1o2+7NsGbZyuGWhUUhPZxviWqDveqajhmL6TjmH4eGyJG-kuCCABiugDBATR3p0f6jFBjKoYdgq8mcZevY8beybDo+Y6Zq+U65iU8wSUUUlkfAgCssYAe7qKcKdYqRKTHqXBbFOTpqp6Te6GGQ+aZPuOWZvtOv6EfOkklNJ8DkYA-pGAFeBgDdNoAXMpeq5EENnuHlqUeGnwexqWZdGuncYFSZDiFgk4RF5kfmgP7xXZgDNNpULngTueVQQeMEsSeCqdX5KF9rxGFGaFJnCXhUWWfAnitdQCVAoA6srddu9H5dBzHHpp2gbWNV6of2QW1QJ2HhWZokEUt1lFrZ3KAGp2XXZT1O39Z5RXeWYb0nQFaE1fxWFhaZIn4dFSB2nFq12YAi3mAJn5Hofdt7l7V5rFmMjHoVf5VXA3xmHGUJuGRRZLKII9Dp2YAkCqAOnmW3KZBTaFbB2MKozgOE+dIMkzNZONXd0NuLDNlta9m1oyzfVs4eHPDdoL2bfj436RdoOkw1t1Q4tqAeCtJbcq6SXM25rOqQrQ2HVops89eRNTXV10Q-NlP5qgNOkSbgDzQebuUMQV1sHSVrr+2rp0TQZl1g7N5NNfdyCxRL8PcoAoYqAJkhgAnyulWWbkpFty1bg2h2xWe5+VF4E47fPE9N9U3ZDC1U18qfG-+gC98YAgdoB71QeY79nPaD3DtnZNwVXeDc0U2J4tPZL-6AErpQJ9198ul8VbEr2P0eawLjdu7P90eMR7d-hU3eAPCaecy0XA8DftW9mNfeeR0DdfO1P8fC3rLLIGfBead-yAEcdM2d9A67UfljJWWgwG7w1vzBursZ6J2hhgI2F8EAgOohA-uUCfqK1tjghB1V64u2ngnEWi1IhtyAR3CogBttUALu6a8MbQKHrAlhpCnaTzjkLXWLd8weDobTbkgBVNPAQXHK+DvrsxtiVSRPDP58O1k3d2YkU70KwfAQADaaADDXW+0jPrsMIQotiBi37V3VmQr+-CdbNw9rIBYmCEpJUAPOhRiwLo0tsHTef0FQeKschKOiDyHfwEY4j8kR55iP-IARLlpbGJ8cXPxT8AnaEScoiesc1FHzQYtNwoifb-nakk7xssH5mLLmYMp2SY5a0Fg4jR91TiuLsoATMzAD0dng9eJd0nDy0N09+vMcmNMPqg6hLI1jtO5IAZvtAAXqb00x8iakKkWSM2uYyD4oKoX-fM6BinPX-IAB+VAB+dss3xg8iElXOe-IAA; regionCode=; regionFullName=%E5%85%A8%E9%83%A8',
}

try:
    response = requests.get(
        'https://www.plap.mil.cn/freecms/rest/v1/notice/selectInfoMoreChannel.do?&siteId=404bb030-5be9-4070-85bd-c94b1473e8de&channel=c5bff13f-21ca-4dac-b158-cb40accd3035&currPage=1&pageSize=20&noticeType=&regionCode=&purchaseManner=&title=&openTenderCode=&operationStartTime=&operationEndTime=&selectTimeName=&cityOrArea=&purchaseNature=&punishType=',
    
        headers=headers,
    )
    if response.status_code == 200:
        data = json.loads(response.text)
        item1= data['data'][0]

        print(item1["id"])
    else:
        raise Exception(f"Request failed with status code {response.status_code}")    
except Exception as e:
    print(f"An error occurred: ERROR{e}")    
    
    