import speedtest

teste = speedtest.Speedtest()

# Download
velocidade_download = teste.download() / 10**6

# Upload
velocidade_upload = teste.upload() / 10**6

# Latência (ping)
velocidade_latencia = teste.results.ping

print('Teste de velocidade da internet...\n')
print(f'Velocidade de download: {velocidade_download:.2f} Mb.')
print(f'Velocidade de upload: {velocidade_upload:.2f} Mb.')
print(f'Velocidade de latência (ping): {velocidade_latencia:.2f}.')