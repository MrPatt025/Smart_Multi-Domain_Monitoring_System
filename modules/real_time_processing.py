import asyncio

async def process_data(data):
    print(f"Processing data: {data}")
    await asyncio.sleep(1)  # จำลองการประมวลผล
    print(f"Finished processing: {data}")

async def main():
    data_stream = ["data1", "data2", "data3"]
    tasks = [process_data(data) for data in data_stream]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())

