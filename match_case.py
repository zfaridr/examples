def main1(values: list | tuple):
    if len(values) == 2 and values[0] == 'load':
        print(f"main1, {values=}, link={values[1].__repr__()}")
    else:
        print("default")

def main2(values: list | tuple):
    match values:
        case "load", link:
            print(f"main2, {values=}, {link=}")
        case _:
            print("default")


def download_files(values: list):
    match values:
        case 'dowmload', file_url:
            print(f"dowmload file: {file_url}")
        case "download", file, *file_urls:
            print(f"download files: {file, file_urls}")
        case _:
            print("default")

def client_hello(server_code):
    match server_code:
        case 1 | 2 | 3:
            print('connection established')
        case _:
            print('no connection')

def get_color(color):
    match color:
        case(r, g, b):
            print("RGB")
        case(r, g, b, a):
            print('RGBA')
        case _:
            print('no template')

print('results of fuctions')

get_color([120, 120, 120])
get_color([120, 120, 120, 0.5])
get_color([120, 120])


client_hello(1)
client_hello('2')


download_files(['download', 'file1', 'file2', 'file3'])
download_files(['download', 'file5'])
download_files(['hello world'])

main1(["load", '123'])
main2(['load', '678'])