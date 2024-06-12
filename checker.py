import json
import quanchecker

urls = ["http://localhost:(port)/image"]

headers = [{
  'Content-Type': 'application/json'
}]

test_cases = [
    {
        'checking_method': quanchecker.response_hash_check,
        'url': urls[0],
        'header': headers[0],
        'method': 'POST',
        'body': json.dumps({
            "image_name": "side0ym19aj.png"
        }),
        'expected': "4E9587AD983044CE3DA1A6B747AF051376592B573105A1CD7C160C7731DE143B",
    },
    {
        'checking_method': quanchecker.response_hash_check,
        'url': urls[0],
        'header': headers[0],
        'method': 'POST',
        'body': json.dumps({
            "image_name": "2la0fk-s.csv.jpg"
        }),
        'expected': "F5FD7D9168CFF19E115A78F85811439BBC5E74DACFEE6E65291800F0481209A8",
    },
    {
        'checking_method': quanchecker.response_based_check,
        'url': urls[0],
        'header': headers[0],
        'method': 'POST',
        'body': json.dumps({
            "image_name": "secret.txt"
        }),
        'expected': { "detail": "Unsupported file type" },
    },
    {
        'checking_method': quanchecker.response_based_check,
        'url': urls[0],
        'header': headers[0],
        'method': 'POST',
        'body': json.dumps({
            "image_name": "secret_none.png"
        }),
        'expected': { "detail": "Image not found" },
    },
    {
        'checking_method': quanchecker.response_based_check,
        'url': urls[0],
        'header': headers[0],
        'method': 'POST',
        'body': json.dumps({
            "image_name": "..\\secret 2.csv"
        }),
        'expected': { "detail": "Invalid image name" },
    }
]

quanchecker.run_tests_dev(test_cases)