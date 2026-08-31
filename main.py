from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
import pysmile
import pysmile_license as pysmile_license  # 6 months only
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)

app.mount("/static", StaticFiles(directory="frontend"), name="static")


class InferRequest(BaseModel):
    evidence: dict


@app.get("/")
async def home():
    return FileResponse("frontend/index.html")


@app.post("/api/infer")
async def infer(req: InferRequest):
    net = pysmile.Network()
    net.read_file("VentureBN.xdsl")
    for node, value in req.evidence.items():
        net.set_evidence(node, value)
    net.update_beliefs()
    beliefs = net.get_node_value("Success")
    outcomes = []
    for i in range(len(beliefs)):
        outcomes.append(
            {
                "id": net.get_outcome_id("Success", i),
                "label": net.get_outcome_id("Success", i),
                "probability": beliefs[i],
                "color": ["#10B981", "#F59E0B", "#EF4444"][i % 3],
            }
        )
    return {"target_node": "Success", "outcomes": outcomes}
