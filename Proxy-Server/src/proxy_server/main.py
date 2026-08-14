from fastmcp import FastMCP

mcp = FastMCP.as_proxy(
    "https://lonely-blush-flyingfish.fastmcp.app/mcp",
     name="proxy_server",
)


if __name__ == "__main__":
    mcp.run()