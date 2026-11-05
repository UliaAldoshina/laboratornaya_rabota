class CDNClient:
    def __init__(self, origin_url: str, cdn_url: str):
        self.origin_url = origin_url
        self.cdn_url = cdn_url

    def get_resource_url(self, file_path: str, version: str = None) -> str:
        if version:
            name, ext = file_path.rsplit(".", 1)
            file_path = f"{name}.{version}.{ext}"
        return f"{self.cdn_url}/static/{file_path}"

    def get_simulation_headers(self, is_cached: bool = False) -> dict:
        headers = {
            "Cache-Control": "public, max-age=3600",
            "Content-Type": "image/jpeg"
        }
        if is_cached:
            headers["Age"] = "600"
            headers["X-Cache"] = "Hit from CDN"
        else:
            headers["X-Cache"] = "Miss from CDN"
        return headers