import runpod
import time

def handler(event):
    input = event['input']
    instruction = input.get('instruction')
    seconds = input.get('seconds', 0)

    # タスクのプレースホルダー: 必要に応じて画像またはテキスト生成ロジックに置き換えてください
    time.sleep(seconds)
    result = "作成しました！"

    return result

if __name__ == '__main__':
    runpod.serverless.start({'handler': handler})
