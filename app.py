from google.cloud import bigquery
import os
os.environ["GCLOUD_PROJECT"] = "climate-data-452305"
client = bigquery.Client()
import pandas as pd
from datetime import datetime, timedelta
import plotly.io as pio
pio.renderers.default = "plotly_mimetype"
import plotly.graph_objects as go
import dash
from dash import dcc, html, Input, Output
import plotly.graph_objects as go
import pandas as pd
import numpy as np

#call data into df
sql = """
    SELECT id, date, element, value
    FROM `bigquery-public-data.ghcn_d.ghcnd_2025`
    WHERE id 
    IN ("US1UTBE0002",
    "US1UTBE0003",
    "US1UTBE0004",
    "US1UTBE0005",
    "US1UTBE0006",
    "US1UTBE0008",
    "US1UTBE0009",
    "US1UTBE0010",
    "US1UTBE0011",
    "US1UTBE0013",
    "US1UTBE0014",
    "US1UTBE0016",
    "US1UTBE0017",
    "US1UTBE0019",
    "US1UTBE0020",
    "US1UTBV0001",
    "US1UTBV0002",
    "US1UTCH0001",
    "US1UTCH0003",
    "US1UTCH0004",
    "US1UTCH0006",
    "US1UTCH0008",
    "US1UTCH0009",
    "US1UTCH0011",
    "US1UTCH0013",
    "US1UTCH0014",
    "US1UTCH0015",
    "US1UTCH0016",
    "US1UTCH0019",
    "US1UTCH0020",
    "US1UTCH0021",
    "US1UTCH0022",
    "US1UTCH0024",
    "US1UTCH0025",
    "US1UTCH0033",
    "US1UTCH0034",
    "US1UTCH0037",
    "US1UTCH0038",
    "US1UTCH0041",
    "US1UTCH0042",
    "US1UTCH0043",
    "US1UTCH0046",
    "US1UTCH0047",
    "US1UTCH0052",
    "US1UTCH0057",
    "US1UTCR0001",
    "US1UTCR0002",
    "US1UTCR0003",
    "US1UTCR0005",
    "US1UTCR0008",
    "US1UTDC0003",
    "US1UTDC0004",
    "US1UTDG0002",
    "US1UTDV0001",
    "US1UTDV0005",
    "US1UTDV0006",
    "US1UTDV0007",
    "US1UTDV0008",
    "US1UTDV0009",
    "US1UTDV0017",
    "US1UTDV0018",
    "US1UTDV0020",
    "US1UTDV0024",
    "US1UTDV0025",
    "US1UTDV0036",
    "US1UTDV0037",
    "US1UTDV0038",
    "US1UTDV0039",
    "US1UTDV0040",
    "US1UTDV0041",
    "US1UTDV0042",
    "US1UTDV0044",
    "US1UTDV0045",
    "US1UTDV0046",
    "US1UTDV0047",
    "US1UTEM0003",
    "US1UTEM0004",
    "US1UTEM0006",
    "US1UTEM0011",
    "US1UTGF0001",
    "US1UTGF0003",
    "US1UTGF0004",
    "US1UTGF0005",
    "US1UTGR0002",
    "US1UTGR0003",
    "US1UTGR0005",
    "US1UTGR0006",
    "US1UTGR0007",
    "US1UTGR0008",
    "US1UTGR0009",
    "US1UTGR0011",
    "US1UTGR0012",
    "US1UTGR0016",
    "US1UTGR0018",
    "US1UTIR0001",
    "US1UTIR0003",
    "US1UTIR0005",
    "US1UTIR0010",
    "US1UTIR0011",
    "US1UTIR0012",
    "US1UTJB0002",
    "US1UTML0001",
    "US1UTML0003",
    "US1UTML0004",
    "US1UTML0005",
    "US1UTML0007",
    "US1UTML0008",
    "US1UTML0009",
    "US1UTML0010",
    "US1UTML0011",
    "US1UTML0013",
    "US1UTMR0001",
    "US1UTPT0002",
    "US1UTRC0001",
    "US1UTSJ0001",
    "US1UTSJ0003",
    "US1UTSJ0004",
    "US1UTSJ0005",
    "US1UTSJ0006",
    "US1UTSJ0007",
    "US1UTSJ0008",
    "US1UTSJ0009",
    "US1UTSJ0010",
    "US1UTSJ0011",
    "US1UTSL0001",
    "US1UTSL0003",
    "US1UTSL0006",
    "US1UTSL0008",
    "US1UTSL0009",
    "US1UTSL0011",
    "US1UTSL0015",
    "US1UTSL0016",
    "US1UTSL0018",
    "US1UTSL0020",
    "US1UTSL0025",
    "US1UTSL0027",
    "US1UTSL0028",
    "US1UTSL0029",
    "US1UTSL0032",
    "US1UTSL0035",
    "US1UTSL0041",
    "US1UTSL0047",
    "US1UTSL0053",
    "US1UTSL0055",
    "US1UTSL0060",
    "US1UTSL0061",
    "US1UTSL0062",
    "US1UTSL0070",
    "US1UTSL0072",
    "US1UTSL0073",
    "US1UTSL0074",
    "US1UTSL0075",
    "US1UTSL0076",
    "US1UTSL0078",
    "US1UTSL0079",
    "US1UTSL0083",
    "US1UTSL0085",
    "US1UTSL0086",
    "US1UTSL0091",
    "US1UTSL0092",
    "US1UTSL0093",
    "US1UTSL0096",
    "US1UTSL0097",
    "US1UTSL0103",
    "US1UTSL0104",
    "US1UTSL0109",
    "US1UTSL0112",
    "US1UTSL0113",
    "US1UTSL0115",
    "US1UTSL0117",
    "US1UTSL0118",
    "US1UTSL0119",
    "US1UTSL0121",
    "US1UTSL0127",
    "US1UTSL0128",
    "US1UTSL0129",
    "US1UTSL0133",
    "US1UTSL0134",
    "US1UTSL0135",
    "US1UTSL0136",
    "US1UTSM0001",
    "US1UTSM0002",
    "US1UTSM0003",
    "US1UTSM0004",
    "US1UTSM0005",
    "US1UTSM0006",
    "US1UTSM0007",
    "US1UTSM0009",
    "US1UTSM0011",
    "US1UTSM0012",
    "US1UTSM0015",
    "US1UTSM0016",
    "US1UTSP0007",
    "US1UTTL0001",
    "US1UTTL0002",
    "US1UTTL0003",
    "US1UTTL0007",
    "US1UTTL0008",
    "US1UTTL0009",
    "US1UTTL0010",
    "US1UTTL0011",
    "US1UTTL0018",
    "US1UTUN0001",
    "US1UTUN0005",
    "US1UTUN0006",
    "US1UTUN0007",
    "US1UTUN0011",
    "US1UTUN0012",
    "US1UTUN0013",
    "US1UTUN0019",
    "US1UTUN0020",
    "US1UTUN0021",
    "US1UTUT0002",
    "US1UTUT0005",
    "US1UTUT0010",
    "US1UTUT0012",
    "US1UTUT0013",
    "US1UTUT0018",
    "US1UTUT0019",
    "US1UTUT0021",
    "US1UTUT0022",
    "US1UTUT0024",
    "US1UTUT0026",
    "US1UTUT0028",
    "US1UTUT0031",
    "US1UTUT0032",
    "US1UTUT0034",
    "US1UTUT0037",
    "US1UTUT0038",
    "US1UTUT0039",
    "US1UTUT0045",
    "US1UTWB0001",
    "US1UTWB0003",
    "US1UTWB0005",
    "US1UTWB0007",
    "US1UTWB0008",
    "US1UTWB0009",
    "US1UTWB0011",
    "US1UTWB0012",
    "US1UTWB0015",
    "US1UTWB0017",
    "US1UTWB0018",
    "US1UTWB0020",
    "US1UTWB0022",
    "US1UTWB0023",
    "US1UTWB0025",
    "US1UTWB0026",
    "US1UTWB0027",
    "US1UTWB0030",
    "US1UTWG0001",
    "US1UTWG0002",
    "US1UTWG0003",
    "US1UTWG0004",
    "US1UTWG0005",
    "US1UTWG0007",
    "US1UTWG0008",
    "US1UTWG0009",
    "US1UTWG0010",
    "US1UTWG0011",
    "US1UTWG0012",
    "US1UTWG0014",
    "US1UTWG0015",
    "US1UTWG0016",
    "US1UTWG0017",
    "US1UTWG0021",
    "US1UTWG0022",
    "US1UTWG0023",
    "US1UTWG0024",
    "US1UTWS0003",
    "US1UTWS0006",
    "US1UTWS0008",
    "US1UTWS0009",
    "US1UTWS0010",
    "US1UTWS0011",
    "US1UTWY0001",
    "USC00420050",
    "USC00420061",
    "USC00420072",
    "USC00420074",
    "USC00420086",
    "USC00420113",
    "USC00420120",
    "USC00420157",
    "USC00420168",
    "USC00420180",
    "USC00420194",
    "USC00420197",
    "USC00420201",
    "USC00420302",
    "USC00420336",
    "USC00420400",
    "USC00420449",
    "USC00420460",
    "USC00420478",
    "USC00420487",
    "USC00420490",
    "USC00420506",
    "USC00420519",
    "USC00420527",
    "USC00420530",
    "USC00420580",
    "USC00420617",
    "USC00420686",
    "USC00420688",
    "USC00420699",
    "USC00420700",
    "USC00420716",
    "USC00420718",
    "USC00420730",
    "USC00420734",
    "USC00420736",
    "USC00420737",
    "USC00420738",
    "USC00420757",
    "USC00420777",
    "USC00420788",
    "USC00420802",
    "USC00420810",
    "USC00420814",
    "USC00420819",
    "USC00420820",
    "USC00420841",
    "USC00420849",
    "USC00420900",
    "USC00420924",
    "USC00420928",
    "USC00421006",
    "USC00421007",
    "USC00421008",
    "USC00421020",
    "USC00421023",
    "USC00421030",
    "USC00421050",
    "USC00421070",
    "USC00421144",
    "USC00421149",
    "USC00421160",
    "USC00421162",
    "USC00421163",
    "USC00421168",
    "USC00421171",
    "USC00421214",
    "USC00421216",
    "USC00421218",
    "USC00421222",
    "USC00421230",
    "USC00421240",
    "USC00421241",
    "USC00421243",
    "USC00421256",
    "USC00421258",
    "USC00421259",
    "USC00421260",
    "USC00421272",
    "USC00421273",
    "USC00421285",
    "USC00421308",
    "USC00421367",
    "USC00421418",
    "USC00421432",
    "USC00421440",
    "USC00421446",
    "USC00421450",
    "USC00421472",
    "USC00421500",
    "USC00421590",
    "USC00421601",
    "USC00421685",
    "USC00421695",
    "USC00421731",
    "USC00421735",
    "USC00421750",
    "USC00421755",
    "USC00421759",
    "USC00421792",
    "USC00421850",
    "USC00421907",
    "USC00421918",
    "USC00421990",
    "USC00422053",
    "USC00422057",
    "USC00422073",
    "USC00422093",
    "USC00422101",
    "USC00422116",
    "USC00422150",
    "USC00422172",
    "USC00422173",
    "USC00422233",
    "USC00422235",
    "USC00422246",
    "USC00422252",
    "USC00422253",
    "USC00422255",
    "USC00422257",
    "USC00422258",
    "USC00422294",
    "USC00422319",
    "USC00422385",
    "USC00422389",
    "USC00422418",
    "USC00422424",
    "USC00422429",
    "USC00422432",
    "USC00422484",
    "USC00422488",
    "USC00422558",
    "USC00422561",
    "USC00422573",
    "USC00422578",
    "USC00422584",
    "USC00422592",
    "USC00422597",
    "USC00422607",
    "USC00422625",
    "USC00422696",
    "USC00422700",
    "USC00422702",
    "USC00422721",
    "USC00422726",
    "USC00422798",
    "USC00422828",
    "USC00422847",
    "USC00422851",
    "USC00422852",
    "USC00422864",
    "USC00422996",
    "USC00423012",
    "USC00423032",
    "USC00423046",
    "USC00423056",
    "USC00423063",
    "USC00423097",
    "USC00423122",
    "USC00423138",
    "USC00423182",
    "USC00423183",
    "USC00423220",
    "USC00423232",
    "USC00423254",
    "USC00423260",
    "USC00423298",
    "USC00423320",
    "USC00423335",
    "USC00423348",
    "USC00423353",
    "USC00423386",
    "USC00423388",
    "USC00423391",
    "USC00423413",
    "USC00423418",
    "USC00423485",
    "USC00423486",
    "USC00423491",
    "USC00423506",
    "USC00423514",
    "USC00423600",
    "USC00423624",
    "USC00423671",
    "USC00423706",
    "USC00423776",
    "USC00423788",
    "USC00423809",
    "USC00423836",
    "USC00423842",
    "USC00423847",
    "USC00423867",
    "USC00423886",
    "USC00423896",
    "USC00423929",
    "USC00423968",
    "USC00423976",
    "USC00423980",
    "USC00424000",
    "USC00424025",
    "USC00424035",
    "USC00424050",
    "USC00424100",
    "USC00424105",
    "USC00424123",
    "USC00424125",
    "USC00424135",
    "USC00424140",
    "USC00424150",
    "USC00424160",
    "USC00424174",
    "USC00424178",
    "USC00424180",
    "USC00424210",
    "USC00424217",
    "USC00424220",
    "USC00424225",
    "USC00424233",
    "USC00424321",
    "USC00424322",
    "USC00424342",
    "USC00424362",
    "USC00424370",
    "USC00424375",
    "USC00424378",
    "USC00424467",
    "USC00424508",
    "USC00424527",
    "USC00424542",
    "USC00424575",
    "USC00424665",
    "USC00424746",
    "USC00424748",
    "USC00424755",
    "USC00424764",
    "USC00424770",
    "USC00424828",
    "USC00424846",
    "USC00424856",
    "USC00424927",
    "USC00424946",
    "USC00424947",
    "USC00424968",
    "USC00424970",
    "USC00425025",
    "USC00425034",
    "USC00425040",
    "USC00425065",
    "USC00425082",
    "USC00425105",
    "USC00425138",
    "USC00425148",
    "USC00425163",
    "USC00425182",
    "USC00425183",
    "USC00425186",
    "USC00425190",
    "USC00425194",
    "USC00425215",
    "USC00425217",
    "USC00425219",
    "USC00425229",
    "USC00425247",
    "USC00425252",
    "USC00425268",
    "USC00425330",
    "USC00425352",
    "USC00425377",
    "USC00425402",
    "USC00425406",
    "USC00425457",
    "USC00425465",
    "USC00425477",
    "USC00425483",
    "USC00425488",
    "USC00425530",
    "USC00425582",
    "USC00425607",
    "USC00425610",
    "USC00425654",
    "USC00425699",
    "USC00425705",
    "USC00425723",
    "USC00425733",
    "USC00425795",
    "USC00425805",
    "USC00425807",
    "USC00425810",
    "USC00425812",
    "USC00425815",
    "USC00425826",
    "USC00425837",
    "USC00425847",
    "USC00425892",
    "USC00425897",
    "USC00425900",
    "USC00425906",
    "USC00425921",
    "USC00425930",
    "USC00425958",
    "USC00425963",
    "USC00425969",
    "USC00425971",
    "USC00425974",
    "USC00425982",
    "USC00426053",
    "USC00426076",
    "USC00426123",
    "USC00426135",
    "USC00426140",
    "USC00426170",
    "USC00426181",
    "USC00426340",
    "USC00426357",
    "USC00426400",
    "USC00426404",
    "USC00426405",
    "USC00426414",
    "USC00426455",
    "USC00426534",
    "USC00426538",
    "USC00426551",
    "USC00426558",
    "USC00426560",
    "USC00426565",
    "USC00426568",
    "USC00426590",
    "USC00426601",
    "USC00426639",
    "USC00426640",
    "USC00426644",
    "USC00426648",
    "USC00426650",
    "USC00426651",
    "USC00426652",
    "USC00426658",
    "USC00426660",
    "USC00426686",
    "USC00426708",
    "USC00426724",
    "USC00426726",
    "USC00426750",
    "USC00426845",
    "USC00426865",
    "USC00426867",
    "USC00426869",
    "USC00426874",
    "USC00426897",
    "USC00426910",
    "USC00426915",
    "USC00426919",
    "USC00426938",
    "USC00427015",
    "USC00427026",
    "USC00427050",
    "USC00427052",
    "USC00427061",
    "USC00427064",
    "USC00427068",
    "USC00427155",
    "USC00427165",
    "USC00427185",
    "USC00427220",
    "USC00427255",
    "USC00427260",
    "USC00427271",
    "USC00427318",
    "USC00427343",
    "USC00427395",
    "USC00427408",
    "USC00427415",
    "USC00427421",
    "USC00427438",
    "USC00427450",
    "USC00427501",
    "USC00427516",
    "USC00427525",
    "USC00427540",
    "USC00427557",
    "USC00427559",
    "USC00427565",
    "USC00427576",
    "USC00427578",
    "USC00427582",
    "USC00427606",
    "USC00427608",
    "USC00427655",
    "USC00427661",
    "USC00427686",
    "USC00427714",
    "USC00427720",
    "USC00427724",
    "USC00427729",
    "USC00427735",
    "USC00427740",
    "USC00427742",
    "USC00427744",
    "USC00427747",
    "USC00427753",
    "USC00427800",
    "USC00427835",
    "USC00427846",
    "USC00427850",
    "USC00427885",
    "USC00427895",
    "USC00427909",
    "USC00427924",
    "USC00427927",
    "USC00427931",
    "USC00427942",
    "USC00427952",
    "USC00427955",
    "USC00427959",
    "USC00428070",
    "USC00428114",
    "USC00428119",
    "USC00428240",
    "USC00428369",
    "USC00428370",
    "USC00428371",
    "USC00428376",
    "USC00428385",
    "USC00428456",
    "USC00428465",
    "USC00428474",
    "USC00428476",
    "USC00428478",
    "USC00428555",
    "USC00428600",
    "USC00428631",
    "USC00428640",
    "USC00428668",
    "USC00428672",
    "USC00428674",
    "USC00428676",
    "USC00428705",
    "USC00428733",
    "USC00428741",
    "USC00428771",
    "USC00428780",
    "USC00428785",
    "USC00428817",
    "USC00428828",
    "USC00428847",
    "USC00428852",
    "USC00428885",
    "USC00428900",
    "USC00428902",
    "USC00428922",
    "USC00428939",
    "USC00428973",
    "USC00428978",
    "USC00429045",
    "USC00429050",
    "USC00429111",
    "USC00429133",
    "USC00429136",
    "USC00429140",
    "USC00429152",
    "USC00429165",
    "USC00429175",
    "USC00429302",
    "USC00429320",
    "USC00429346",
    "USC00429365",
    "USC00429368",
    "USC00429383",
    "USC00429419",
    "USC00429468",
    "USC00429490",
    "USC00429491",
    "USC00429514",
    "USC00429560",
    "USC00429575",
    "USC00429584",
    "USC00429595",
    "USC00429629",
    "USC00429675",
    "USC00429679",
    "USC00429717",
    "USC00429725",
    "USR0000AQUA",
    "USR0000ARAG",
    "USR0000ASSA",
    "USR0000BADG",
    "USR0000BARN",
    "USR0000BEAR",
    "USR0000BIGI",
    "USR0000BKTL",
    "USR0000BLAC",
    "USR0000BRIM",
    "USR0000BRUN",
    "USR0000BRYC",
    "USR0000BRYS",
    "USR0000BUCF",
    "USR0000BUES",
    "USR0000CART",
    "USR0000CEDM",
    "USR0000CHEP",
    "USR0000COTT",
    "USR0000CRAT",
    "USR0000DIAM",
    "USR0000ENSI",
    "USR0000ENTR",
    "USR0000FIVE",
    "USR0000FTOP",
    "USR0000HEWI",
    "USR0000HORR",
    "USR0000HORS",
    "USR0000JENS",
    "USR0000JOES",
    "USR0000KANE",
    "USR0000KING",
    "USR0000LAVA",
    "USR0000LOST",
    "USR0000MCCO",
    "USR0000MINE",
    "USR0000MUDS",
    "USR0000MUSK",
    "USR0000NLPT",
    "USR0000NORW",
    "USR0000OTTE",
    "USR0000PARI",
    "USR0000PLGV",
    "USR0000RAYS",
    "USR0000REDD",
    "USR0000ROSE",
    "USR0000SAND",
    "USR0000SEGO",
    "USR0000SEVI",
    "USR0000SIGN",
    "USR0000SIMP",
    "USR0000SKUN",
    "USR0000TELE",
    "USR0000TOMB",
    "USR0000TULE",
    "USR0000UGB1",
    "USR0000UPRC",
    "USR0000VERN",
    "USR0000WEFK",
    "USS0009J01S",
    "USS0009J05S",
    "USS0009J08S",
    "USS0009J16S",
    "USS0009K01S",
    "USS0009L01S",
    "USS0009L03S",
    "USS0009M01S",
    "USS0009M02S",
    "USS0010J01S",
    "USS0010J04S",
    "USS0010J06S",
    "USS0010J10S",
    "USS0010J12S",
    "USS0010J17S",
    "USS0010J18S",
    "USS0010J20S",
    "USS0010J21S",
    "USS0010J22S",
    "USS0010J23S",
    "USS0010J25S",
    "USS0010J26S",
    "USS0010J30S",
    "USS0010J35S",
    "USS0010J43S",
    "USS0010J44S",
    "USS0010J52S",
    "USS0010J55S",
    "USS0010K01S",
    "USS0010K02S",
    "USS0010k05s",
    "USS0010K06S",
    "USS0010M01S",
    "USS0011H01S",
    "USS0011H03S",
    "USS0011H07S",
    "USS0011H08S",
    "USS0011H21S",
    "USS0011H25S",
    "USS0011H30S",
    "USS0011H31S",
    "USS0011H32S",
    "USS0011H36S",
    "USS0011H37S",
    "USS0011H55S",
    "USS0011H57S",
    "USS0011H58S",
    "USS0011H59S",
    "USS0011H60S",
    "USS0011J01S",
    "USS0011J02S",
    "USS0011J06S",
    "USS0011J08S",
    "USS0011J11S",
    "USS0011J12S",
    "USS0011J21S",
    "USS0011J22S",
    "USS0011J23S",
    "USS0011J32S",
    "USS0011J37S",
    "USS0011J42S",
    "USS0011J46S",
    "USS0011J52S",
    "USS0011J53S",
    "USS0011J56S",
    "USS0011J57S",
    "USS0011J64S",
    "USS0011J65S",
    "USS0011J68S",
    "USS0011J69S",
    "USS0011J70S",
    "USS0011K03S",
    "USS0011K05S",
    "USS0011K09S",
    "USS0011K10S",
    "USS0011K11S",
    "USS0011K12S",
    "USS0011K13S",
    "USS0011K15S",
    "USS0011K21S",
    "USS0011K22S",
    "USS0011K28S",
    "USS0011K29S",
    "USS0011K31S",
    "USS0011K32S",
    "USS0011K35S",
    "USS0011K36S",
    "USS0011K39S",
    "USS0011K52S",
    "USS0011L01S",
    "USS0011L02S",
    "USS0011L03S",
    "USS0011L04S",
    "USS0011L05S",
    "USS0011L12S",
    "USS0011M01S",
    "USS0011M03S",
    "USS0011M06S",
    "USS0012J02S",
    "USS0012J06S",
    "USS0012J07S",
    "USS0012J09S",
    "USS0012K01S",
    "USS0012K02S",
    "USS0012L04S",
    "USS0012L05S",
    "USS0012L06S",
    "USS0012L07S",
    "USS0012L12S",
    "USS0012L15S",
    "USS0012L20S",
    "USS0012M03S",
    "USS0012M05S",
    "USS0012M06S",
    "USS0012M07S",
    "USS0012M11S",
    "USS0012M13S",
    "USS0012M14S",
    "USS0012M17S",
    "USS0012M23S",
    "USS0012M26S",
    "USS0013H05S",
    "USS0013M02S",
    "USS0013M04S",
    "USS0013M05S",
    "USS0013M06S",
    "USS0013M07S",
    "USSNRCS0124",
    "USW00003081",
    "USW00004134",
    "USW00004138",
    "USW00004143",
    "USW00023159",
    "USW00023162",
    "USW00023170",
    "USW00023176",
    "USW00023177",
    "USW00023186",
    "USW00024101",
    "USW00024103",
    "USW00024111",
    "USW00024120",
    "USW00024122",
    "USW00024125",
    "USW00024126",
    "USW00024127",
    "USW00024175",
    "USW00024193",
    "USW00053004",
    "USW00053010",
    "USW00053012",
    "USW00053013",
    "USW00053014",
    "USW00053023",
    "USW00053149",
    "USW00053165",
    "USW00053166",
    "USW00053167",
    "USW00053171",
    "USW00053174",
    "USW00053185",
    "USW00093075",
    "USW00093129",
    "USW00093141",
    "USW00093198",
    "USW00094030",
    "USW00094096",
    "USW00094097",
    "USW00094098",
    "USW00094128",
    "USW00094138")
        
"""

df = client.query_and_wait(sql).to_dataframe()

# This f-er lets you modify df_25_P without modifying df and causing an error
pd.options.mode.copy_on_write = True

#convert string 'date' to datetime 'brentrocks'
df['brentrocks'] = pd.to_datetime(df['date'], format = '%Y-%m-%d')

#convert datetime 'brentrocks' into 'axisdate' and normalized the year
df['axisdate'] = pd.to_datetime(df['brentrocks'].dt.strftime('2025-%m-%d'),format = '%Y-%m-%d', errors="coerce")

#filters out leap year
df = df[df.axisdate.notnull()]

# PRCP
#filter 2025 by element
df_25_P = df[df['element'] == 'PRCP']

df_25_P["Daily Average"] = df_25_P.groupby("axisdate")["value"].transform('mean')

#make a df that ignores every column except what you'll graph
df_25_P_near = df_25_P[['axisdate', 'Daily Average']]
# make a df_go that drops duplicate values and is ready to graph
df_25_PRCP_go = df_25_P_near.drop_duplicates()
yesterday = datetime.now() - timedelta(days = 4)
df_25_PRCP_go = df_25_PRCP_go[(df_25_PRCP_go["axisdate"]<=yesterday)]

#SNWD filter 2025 by element
df_25_SNWD = df[df['element'] == 'SNWD']

df_25_SNWD["Daily Average"] = df_25_SNWD.groupby("axisdate")["value"].transform('mean')

#make a df that ignores every column except what you'll graph
df_25_SNWD_near = df_25_SNWD[['axisdate', 'Daily Average']]

# make a df_go that drops duplicate values and is ready to graph
df_25_SNWD_go = df_25_SNWD_near.drop_duplicates()

# Waits a while before showing data to allow it time to update completely
df_25_SNWD_go = df_25_SNWD_go[(df_25_SNWD_go["axisdate"]<=yesterday)]

# TMIN / TMAX
#filter 2025 by element
df_25_TMIN = df[df['element'] == 'TMIN']

#filter 2025 by element
df_25_TMAX = df[df['element'] == 'TMAX']

#average same-day values
df_25_TMIN["Daily Average"] = df_25_TMIN.groupby("axisdate")["value"].transform('mean')

#average same-day values
df_25_TMAX["Daily Average"] = df_25_TMAX.groupby("axisdate")["value"].transform('mean')

#make a df that ignores every column except what you'll graph
df_25_TMIN_near = df_25_TMIN[['axisdate', 'Daily Average']]

#make a df that ignores every column except what you'll graph
df_25_TMAX_near = df_25_TMAX[['axisdate', 'Daily Average']]

# make a df_go that drops duplicate values and is ready to graph
df_25_TMIN_go = df_25_TMIN_near.drop_duplicates()
df_25_TMIN_go['Daily Average'] = df_25_TMIN_go['Daily Average']/10 #gets the units right. Now it's celsius

# make a df_go that drops duplicate values and is ready to graph
df_25_TMAX_go = df_25_TMAX_near.drop_duplicates()
df_25_TMAX_go['Daily Average'] = df_25_TMAX_go['Daily Average']/10 # gets the units right. Now its celsius

# EVAP
#filter 2025 by element
df_25_EVAP = df[df['element'] == 'EVAP']


df_25_EVAP["Daily Average"] = df_25_EVAP.groupby("axisdate")["value"].transform('mean')

#make a df that ignores every column except what you'll graph
df_25_EVAP_near = df_25_EVAP[['axisdate', 'Daily Average']]

# make a df_go that drops duplicate values and is ready to graph
df_25_EVAP_go = df_25_EVAP_near.drop_duplicates()

# Waits a while before showing data to allow it time to update completely
df_25_EVAP_go = df_25_EVAP_go[(df_25_EVAP_go["axisdate"]<=yesterday)]

# SNOW
#filter 2025 by element
df_25_SNOW = df[df['element'] == 'SNOW']

#take a mean for every day
df_25_SNOW["Daily Average"] = df_25_SNOW.groupby("axisdate")["value"].transform('mean')

#make a df that ignores every column except what you'll graph
df_25_SNOW_near = df_25_SNOW[['axisdate', 'Daily Average']]

# make a df_go that drops duplicate values and is ready to graph
df_25_SNOW_go = df_25_SNOW_near.drop_duplicates()

# Waits a while before showing data to allow it time to update completely
df_25_SNOW_go = df_25_SNOW_go[(df_25_SNOW_go["axisdate"]<=yesterday)]

# WESD
#filter 2025 by element
df_25_WESD = df[df['element'] == 'WESD']

#take a mean for every day
df_25_WESD["Daily Average"] = df_25_WESD.groupby("axisdate")["value"].transform('mean')

#make a df that ignores every column except what you'll graph
df_25_WESD_near = df_25_WESD[['axisdate', 'Daily Average']]

# make a df_go that drops duplicate values and is ready to graph
df_25_WESD_go = df_25_WESD_near.drop_duplicates()
df_25_WESD_go = df_25_WESD_go[(df_25_WESD_go["axisdate"]<=yesterday)]

# AWND
#filter 2025 by element
df_25_AWND = df[df['element'] == 'AWND']

#take a mean for every day
df_25_AWND["Daily Average"] = df_25_AWND.groupby("axisdate")["value"].transform('mean')

#make a df that ignores every column except what you'll graph
df_25_AWND_near = df_25_AWND[['axisdate', 'Daily Average']]

# make a df_go that drops duplicate values and is ready to graph
df_25_AWND_go = df_25_AWND_near.drop_duplicates()
df_25_AWND_go['Daily Average'] = df_25_AWND_go['Daily Average']/10 # fixes units into km/h

# Waits a while before showing data to allow it time to update completely
df_25_AWND_go = df_25_AWND_go[(df_25_AWND_go["axisdate"]<=yesterday)]

# SN33 / SX33
#filter 2025 by element
df_25_SN33 = df[df['element'] == 'SN33']

#take a mean for every day
df_25_SN33["Daily Average"] = df_25_SN33.groupby("axisdate")["value"].transform('mean')

#make a df that ignores every column except what you'll graph
df_25_SN33_near = df_25_SN33[['axisdate', 'Daily Average']]

# make a df_go that drops duplicate values and is ready to graph
df_25_SN33_go = df_25_SN33_near.drop_duplicates()
df_25_SN33_go['Daily Average'] = df_25_SN33_go['Daily Average']/10 # fixes units into celsius

#filter 2025 by element
df_25_SX33 = df[df['element'] == 'SX33']

#take a mean for every day
df_25_SX33["Daily Average"] = df_25_SX33.groupby("axisdate")["value"].transform('mean')

#make a df that ignores every column except what you'll graph
df_25_SX33_near = df_25_SX33[['axisdate', 'Daily Average']]

# make a df_go that drops duplicate values and is ready to graph
df_25_SX33_go = df_25_SX33_near.drop_duplicates()
df_25_SX33_go['Daily Average'] = df_25_SX33_go['Daily Average']/10 # fixes units into celsius

# WSFI
#filter 2025 by element
df_25_WSFI = df[df['element'] == 'WSFI']

#take a mean for every day
df_25_WSFI["Daily Average"] = df_25_WSFI.groupby("date")["value"].transform('mean')

#make a df that ignores every column except what you'll graph
df_25_WSFI_near = df_25_WSFI[['axisdate', 'Daily Average']]

# make a df_go that drops duplicate values and is ready to graph
df_25_WSFI_go = df_25_WSFI_near.drop_duplicates()
df_25_WSFI_go['Daily Average'] = df_25_WSFI_go['Daily Average']/10 # fixes units into km/h

# Waits a while before showing data to allow it time to update completely
df_25_WSFI_go = df_25_WSFI_go[(df_25_WSFI_go["axisdate"]<=yesterday)]

#define a df by reading your decades df csv file
df_all = pd.read_csv('df_all.csv', sep=",")

# DECADES
# PRCP
#Filter Big One by element
df_PRCP = df_all[df_all['element'] == 'PRCP']
df_PRCP = df_PRCP.sort_values(by='axisdate')  

#take an the average of everything that has each month/day combo, make it a new column.
df_PRCP["Daily Average"] = df_PRCP.groupby("date")["value"].transform('mean')

#make a df that ignores every column except what you'll graph
df_PRCP_near = df_PRCP[['axisdate', 'Daily Average']]

#drop every duplicate value, making a df_go that is ready to graph
df_PRCP_go = df_PRCP_near.drop_duplicates()

# SNWD
#Filter Big One by element
df_SNWD = df_all[df_all['element'] == 'SNWD']
df_SNWD = df_SNWD.sort_values(by='axisdate')  

#take an the average of everything that has each month/day combo, make it a new column.
df_SNWD["Daily Average"] = df_SNWD.groupby("date")["value"].transform('mean')

#make a df that ignores every column except what you'll graph
df_SNWD_near = df_SNWD[['axisdate', 'Daily Average']]

#drop every duplicate value, making a df_go that is ready to graph
df_SNWD_go = df_SNWD_near.drop_duplicates()

# TMIN / TMAX
#filter 2025 by element
df_TMIN = df_all[df_all['element'] == 'TMIN']

#filter 2025 by element
df_TMAX = df_all[df_all['element'] == 'TMAX']

#average same-day values
df_TMIN["Daily Average"] = df_TMIN.groupby("date")["value"].transform('mean')

#average same-day values
df_TMAX["Daily Average"] = df_TMAX.groupby("date")["value"].transform('mean')

#make a df that ignores every column except what you'll graph
df_TMIN_near = df_TMIN[['axisdate', 'Daily Average']]

#make a df that ignores every column except what you'll graph
df_TMAX_near = df_TMAX[['axisdate', 'Daily Average']]

# make a df_go that drops duplicate values and is ready to graph
df_TMIN_go = df_TMIN_near.drop_duplicates()
df_TMIN_go['Daily Average'] = df_TMIN_go['Daily Average']/10 # fixes units into celsius

# make a df_go that drops duplicate values and is ready to graph
df_TMAX_go = df_TMAX_near.drop_duplicates()
df_TMAX_go['Daily Average'] = df_TMAX_go['Daily Average']/10 # fixes units into celsius

# EVAP
#filter 2025 by element
df_EVAP = df_all[df_all['element'] == 'EVAP']

df_EVAP["Daily Average"] = df_EVAP.groupby("date")["value"].transform('mean')

#make a df that ignores every column except what you'll graph
df_EVAP_near = df_EVAP[['axisdate', 'Daily Average']]

# make a df_go that drops duplicate values and is ready to graph
df_EVAP_go = df_EVAP_near.drop_duplicates()

# SNOW
#filter by element
df_SNOW = df_all[df_all['element'] == 'SNOW']


#take a mean for every day
df_SNOW["Daily Average"] = df_SNOW.groupby("date")["value"].transform('mean')


#make a df that ignores every column except what you'll graph
df_SNOW_near = df_SNOW[['axisdate', 'Daily Average']]


# make a df_go that drops duplicate values and is ready to graph
df_SNOW_go = df_SNOW_near.drop_duplicates()

# WESD
#filter by element
df_WESD = df_all[df_all['element'] == 'WESD']

#take a mean for every day
df_WESD["Daily Average"] = df_WESD.groupby("date")["value"].transform('mean')

#make a df that ignores every column except what you'll graph
df_WESD_near = df_WESD[['axisdate', 'Daily Average']]

# make a df_go that drops duplicate values and is ready to graph
df_WESD_go = df_WESD_near.drop_duplicates()
df_WESD_go = df_WESD_go.sort_values(by="axisdate")

# AWND
#filter by element
df_AWND = df_all[df_all['element'] == 'AWND']

#take a mean for every day
df_AWND["Daily Average"] = df_AWND.groupby("date")["value"].transform('mean').abs()

#make a df that ignores every column except what you'll graph
df_AWND_near = df_AWND[['axisdate', 'Daily Average']]

# make a df_go that drops duplicate values and is ready to graph
df_AWND_go = df_AWND_near.drop_duplicates()
df_AWND_go['Daily Average'] = df_AWND_go['Daily Average']/10 # fixes units into km/h

# SN33 / SX33
#filter by element
df_SN33 = df_all[df_all['element'] == 'SN33']

#take a mean for every day
df_SN33["Daily Average"] = df_SN33.groupby("date")["value"].transform('mean')

#make a df that ignores every column except what you'll graph
df_SN33_near = df_SN33[['axisdate', 'Daily Average']]

# make a df_go that drops duplicate values and is ready to graph
df_SN33_go = df_SN33_near.drop_duplicates()
df_SN33_go['Daily Average'] = df_SN33_go['Daily Average']/10 # fixes units into celsius

#filter by element
df_SX33 = df_all[df_all['element'] == 'SX33']

#take a mean for every day
df_SX33["Daily Average"] = df_SX33.groupby("date")["value"].transform('mean')

#make a df that ignores every column except what you'll graph
df_SX33_near = df_SX33[['axisdate', 'Daily Average']]

# make a df_go that drops duplicate values and is ready to graph
df_SX33_go = df_SX33_near.drop_duplicates()
df_SX33_go['Daily Average'] = df_SX33_go['Daily Average']/10 # fixes units into celsius

# WSFI
#filter by element
df_WSFI = df_all[df_all['element'] == 'WSFI']

#take a mean for every day
df_WSFI["Daily Average"] = df_WSFI.groupby("date")["value"].transform('mean').abs()

#make a df that ignores every column except what you'll graph
df_WSFI_near = df_WSFI[['axisdate', 'Daily Average']]

df_WSFI_nearer = df_WSFI_near.mask(df_WSFI_near["Daily Average"] > 400)

# make a df_go that drops duplicate values and is ready to graph
df_WSFI_go = df_WSFI_nearer.drop_duplicates()
df_WSFI_go['Daily Average'] = df_WSFI_go['Daily Average']/10 # fixes units into km/h

# Plots

#PRCP - Precipitation

hue = 'steelblue' #line color of graph
canvas = 'aliceblue' #background color
reference = 'lightsteelblue' #color of reference line

df_PRCP_go = df_PRCP_go.sort_values(by="axisdate")
df_25_PRCP_go = df_25_PRCP_go.sort_values(by="axisdate")

fig_PRCP = go.Figure ()
fig_PRCP.add_trace(go.Scatter(x = df_PRCP_go["axisdate"],
                        y = df_PRCP_go["Daily Average"],
                        mode = "lines",
                        name = "Decade Average",
                        hoverinfo = 'none',
                        #connectgaps = False,
                        line = dict(color = reference,
                                    #shape = 'spline',
                                    width = 1)))
fig_PRCP.add_trace(go.Scatter(x = df_25_PRCP_go["axisdate"],
                         y = df_25_PRCP_go["Daily Average"],
                         mode = "lines",
                         name = "2025",
                         connectgaps = True,
                         line = dict(color = hue,
                                     shape = 'spline',
                                     width = 3)))
fig_PRCP.update_layout(plot_bgcolor = canvas,
                  paper_bgcolor = canvas,
                  legend_font_color = hue,
                  legend_orientation = 'h',
                  legend_yanchor = 'top',
                  legend_y = 1.15,
                  legend_xanchor = 'right',
                  legend_x = 1,
                  title = dict(text = "PRECIPITATION",
                               font_color = hue,
                               xanchor = 'left',
                               x = 0.074,
                               font_size = 25,
                               yanchor = 'top',
                               y = 0.84)
                               )
    
fig_PRCP.update_xaxes(color = hue,
                gridcolor = hue,
                linecolor = hue,
                mirror = True,
                showgrid = False,
                ticks = "inside",
                ticklen = 5,
                tickformat= "%b %d",
                nticks = 12,
                title = dict(text = ""),
                )
fig_PRCP.update_yaxes(color = hue,
                 gridcolor = hue,
                 linecolor = hue,
                 mirror = True,
                 showgrid = True,
                 ticks = 'inside',
                 ticklen = 5,
                 zeroline = False,
                 rangemode = 'tozero',
                 title = dict(text = "Precipitation (mm)")
                 )

fig_PRCP.show()

#SNWD - Snow Depth

hue = 'slategrey' #line color of graph
canvas = 'whitesmoke' #background color
reference = 'silver' #color of reference line

df_SNWD_go = df_SNWD_go.sort_values(by="axisdate")
df_25_SNWD_go = df_25_SNWD_go.sort_values(by="axisdate")

fig_SNWD = go.Figure ()
fig_SNWD.add_trace(go.Scatter(x = df_SNWD_go["axisdate"],
                        y = df_SNWD_go["Daily Average"],
                        mode = "lines",
                        name = "Decade Average",
                        connectgaps = True,
                        hoverinfo = 'none',
                        line = dict(color = reference,
                                    shape = 'spline',
                                    width = 1)))
fig_SNWD.add_trace(go.Scatter(x = df_25_SNWD_go["axisdate"],
                         y = df_25_SNWD_go["Daily Average"],
                         mode = "lines",
                         name = "2025",
                         connectgaps = True,
                         line = dict(color = hue,
                                     shape = 'spline',
                                     width = 3)))
fig_SNWD.update_layout(plot_bgcolor = canvas,
                  paper_bgcolor = canvas,
                  legend_font_color = hue,
                  legend_orientation = 'h',
                  legend_yanchor = 'top',
                  legend_y = 1.15,
                  legend_xanchor = 'right',
                  legend_x = 1,
                  title = dict(text = "SNOW DEPTH",
                               font_color = hue,
                               xanchor = 'left',
                               x = 0.074,
                               font_size = 25,
                               yanchor = 'top',
                               y = 0.84)
                               )
    
fig_SNWD.update_xaxes(color = hue,
                gridcolor = hue,
                linecolor = hue,
                mirror = True,
                showgrid = False,
                ticks = "inside",
                ticklen = 5,
                tickformat= "%b %d",
                nticks = 12,
                title = dict(text = ""),
                )
fig_SNWD.update_yaxes(color = hue,
                 gridcolor = hue,
                 linecolor = hue,
                 mirror = True,
                 showgrid = True,
                 ticks = 'inside',
                 ticklen = 5,
                 zeroline = False,
                 rangemode = 'tozero',
                 title = dict(text = "Snow Depth (mm)")
                 )

fig_SNWD.show()
### TMIN / TMAX
#TMIN / TMAX - Min and Max Temp

hue = 'slategrey' #line color of graph
canvas = 'whitesmoke' #background color
referencemin = 'lightsteelblue' #color of reference line
referencemax = 'salmon'
mincolor = 'navy'
maxcolor = 'firebrick'

df_TMIN_go = df_TMIN_go.sort_values(by="axisdate")
df_TMAX_go = df_TMAX_go.sort_values(by="axisdate")
df_25_TMIN_go = df_25_TMIN_go.sort_values(by="axisdate")
df_25_TMAX_go = df_25_TMAX_go.sort_values(by="axisdate")

fig_TMIN = go.Figure ()
fig_TMIN.add_trace(go.Scatter(x = df_TMIN_go["axisdate"],
                        y = df_TMIN_go["Daily Average"],
                        mode = "lines",
                        name = "Decade (Min)",
                        #connectgaps = False,
                        hoverinfo = 'none',
                        line = dict(color = referencemin,
                                    shape = 'spline',
                                    width = 1)))
fig_TMIN.add_trace(go.Scatter(x = df_TMAX_go["axisdate"],
                        y = df_TMAX_go["Daily Average"],
                        mode = "lines",
                        name = "Decade (Max)",
                        #connectgaps = False,
                        hoverinfo = 'none',
                        line = dict(color = referencemax,
                                    shape = 'spline',
                                    width = 1)))
fig_TMIN.add_trace(go.Scatter(x = df_25_TMIN_go["axisdate"],
                         y = df_25_TMIN_go["Daily Average"],
                         mode = "lines",
                         name = "2025 (Min)",
                         connectgaps = True,
                         line = dict(color = mincolor,
                                     shape = 'spline',
                                     width = 3)))
fig_TMIN.add_trace(go.Scatter(x = df_25_TMAX_go["axisdate"],
                         y = df_25_TMAX_go["Daily Average"],
                         mode = "lines",
                         name = "2025 (Max)",
                         connectgaps = True,
                         line = dict(color = maxcolor,
                                     shape = 'spline',
                                     width = 3)))
fig_TMIN.update_layout(plot_bgcolor = canvas,
                  paper_bgcolor = canvas,
                  legend_font_color = hue,
                  legend_orientation = 'v',
                  legend_yanchor = 'top',
                  legend_y = 1,
                  legend_xanchor = 'right',
                  legend_x = 1,
                  title = dict(text = "MAX / MIN TEMPERATURE",
                               font_color = hue,
                               xanchor = 'left',
                               x = 0.074,
                               font_size = 25,
                               yanchor = 'top',
                               y = 0.84)
                               )
    
fig_TMIN.update_xaxes(color = hue,
                gridcolor = hue,
                linecolor = hue,
                mirror = True,
                showgrid = False,
                ticks = "inside",
                ticklen = 5,
                tickformat= "%b %d",
                nticks = 12,
                title = dict(text = ""),
                )
fig_TMIN.update_yaxes(color = hue,
                 gridcolor = hue,
                 linecolor = hue,
                 mirror = True,
                 showgrid = True,
                 ticks = 'inside',
                 ticklen = 5,
                 zeroline = False,
                 rangemode = 'tozero',
                 title = dict(text = "Temperature (C)")
                 )

fig_TMIN.show()

#EVAP - EVAPORATION

hue = 'teal' #line color of graph
canvas = 'azure' #background color
reference = 'lightblue' #color of reference line

df_EVAP_go = df_EVAP_go.sort_values(by="axisdate")
df_25_EVAP_go = df_25_EVAP_go.sort_values(by="axisdate")

fig_EVAP = go.Figure ()
fig_EVAP.add_trace(go.Scatter(x = df_EVAP_go["axisdate"],
                        y = df_EVAP_go["Daily Average"],
                        mode = "lines",
                        name = "Decade Average",
                        connectgaps = True,
                        hoverinfo = 'none',
                        line = dict(color = reference,
                                    shape = 'spline',
                                    width = 1)))
fig_EVAP.add_trace(go.Scatter(x = df_25_EVAP_go["axisdate"],
                         y = df_25_EVAP_go["Daily Average"],
                         mode = "lines",
                         name = "2025",
                         connectgaps = True,
                         line = dict(color = hue,
                                     shape = 'spline',
                                     width = 3)))
fig_EVAP.update_layout(plot_bgcolor = canvas,
                  paper_bgcolor = canvas,
                  showlegend = True,
                  legend_font_color = hue,
                  legend_orientation = 'h',
                  legend_yanchor = 'top',
                  legend_y = 1.15,
                  legend_xanchor = 'right',
                  legend_x = 1,
                  title = dict(text = "DAILY EVAPORATION",
                               font_color = hue,
                               xanchor = 'left',
                               x = 0.074,
                               font_size = 25,
                               yanchor = 'top',
                               y = 0.84)
                               )
    
fig_EVAP.update_xaxes(color = hue,
                gridcolor = hue,
                linecolor = hue,
                mirror = True,
                showgrid = False,
                ticks = "inside",
                ticklen = 5,
                tickformat= "%b %d",
                nticks = 12,
                range = ['2025-01-01', '2025-12-31'],
                title = dict(text = ""),
                )
fig_EVAP.update_yaxes(color = hue,
                 gridcolor = hue,
                 linecolor = hue,
                 mirror = True,
                 showgrid = True,
                 ticks = 'inside',
                 ticklen = 5,
                 zeroline = False,
                 rangemode = 'tozero',
                 title = dict(text = "Evaporation (mm)")
                 )

fig_EVAP.show()

#SNOW - SNOWFALL

hue = 'darkslateblue' #line color of graph
canvas = 'lavender' #background color
reference = 'thistle' #color of reference line

df_SNOW_go = df_SNOW_go.sort_values(by="axisdate")
df_25_SNOW_go = df_25_SNOW_go.sort_values(by="axisdate")

fig_SNOW = go.Figure ()
fig_SNOW.add_trace(go.Scatter(x = df_SNOW_go["axisdate"],
                        y = df_SNOW_go["Daily Average"],
                        mode = "lines",
                        name = "Decade Average",
                        connectgaps = True,
                        hoverinfo = 'none',
                        line = dict(color = reference,
                                    shape = 'spline',
                                    width = 1)))
fig_SNOW.add_trace(go.Scatter(x = df_25_SNOW_go["axisdate"],
                         y = df_25_SNOW_go["Daily Average"],
                         mode = "lines",
                         name = "2025",
                         connectgaps = True,
                         line = dict(color = hue,
                                     shape = 'spline',
                                     width = 3)))
fig_SNOW.update_layout(plot_bgcolor = canvas,
                  paper_bgcolor = canvas,
                  showlegend = True,
                  legend_font_color = hue,
                  legend_orientation = 'h',
                  legend_yanchor = 'top',
                  legend_y = 1.15,
                  legend_xanchor = 'right',
                  legend_x = 1,
                  title = dict(text = "SNOWFALL",
                               font_color = hue,
                               xanchor = 'left',
                               x = 0.074,
                               font_size = 25,
                               yanchor = 'top',
                               y = 0.84)
                               )
    
fig_SNOW.update_xaxes(color = hue,
                gridcolor = hue,
                linecolor = hue,
                mirror = True,
                showgrid = False,
                ticks = "inside",
                ticklen = 5,
                tickformat= "%b %d",
                nticks = 12,
                range = ['2025-01-01', '2025-12-31'],
                title = dict(text = ""),
                )
fig_SNOW.update_yaxes(color = hue,
                 gridcolor = hue,
                 linecolor = hue,
                 mirror = True,
                 showgrid = True,
                 ticks = 'inside',
                 ticklen = 5,
                 zeroline = False,
                 rangemode = 'tozero',
                 title = dict(text = "Snowfall (mm)")
                 )

fig_SNOW.show()

#WESD - SNOW-WATER EQUIVALENT

hue = 'steelblue' #line color of graph
canvas = 'aliceblue' #background color
reference = 'lightblue' #color of reference line

df_WESD_go = df_WESD_go.sort_values(by="axisdate")
df_25_WESD_go = df_25_WESD_go.sort_values(by="axisdate")

fig_WESD = go.Figure ()
fig_WESD.add_trace(go.Scatter(x = df_WESD_go["axisdate"],
                        y = df_WESD_go["Daily Average"],
                        mode = "lines",
                        name = "Decade Average",
                        connectgaps = True,
                        hoverinfo = 'none',
                        line = dict(color = reference,
                                    shape = 'spline',
                                    width = 1)))
fig_WESD.add_trace(go.Scatter(x = df_25_WESD_go["axisdate"],
                         y = df_25_WESD_go["Daily Average"],
                         mode = "lines",
                         name = "2025",
                         connectgaps = True,
                         line = dict(color = hue,
                                     shape = 'spline',
                                     width = 3)))
fig_WESD.update_layout(plot_bgcolor = canvas,
                  paper_bgcolor = canvas,
                  showlegend = True,
                  legend_font_color = hue,
                  legend_orientation = 'h',
                  legend_yanchor = 'top',
                  legend_y = 1.15,
                  legend_xanchor = 'right',
                  legend_x = 1,
                  title = dict(text = "SNOW WATER EQUIVALENT",
                               font_color = hue,
                               xanchor = 'left',
                               x = 0.074,
                               font_size = 25,
                               yanchor = 'top',
                               y = 0.84)
                               )
    
fig_WESD.update_xaxes(color = hue,
                gridcolor = hue,
                linecolor = hue,
                mirror = True,
                showgrid = False,
                ticks = "inside",
                ticklen = 5,
                tickformat= "%b %d",
                nticks = 12,
                range = ['2025-01-01', '2025-12-31'],
                title = dict(text = ""),
                )
fig_WESD.update_yaxes(color = hue,
                 gridcolor = hue,
                 linecolor = hue,
                 mirror = True,
                 showgrid = True,
                 ticks = 'inside',
                 ticklen = 5,
                 zeroline = False,
                 rangemode = 'tozero',
                 title = dict(text = "Water Equivalent (mm)")
                 )

fig_WESD.show()

#AWND - AVERAGE DAILY WIND SPEED

hue = 'darkgreen' #line color of graph
canvas = 'honeydew' #background color
reference = 'darkseagreen' #color of reference line

df_AWND_go = df_AWND_go.sort_values(by="axisdate")
df_25_AWND_go = df_25_AWND_go.sort_values(by="axisdate")

fig_AWND = go.Figure ()
fig_AWND.add_trace(go.Scatter(x = df_AWND_go["axisdate"],
                        y = df_AWND_go["Daily Average"],
                        mode = "lines",
                        name = "Decade Average",
                        connectgaps = True,
                        hoverinfo = 'none',
                        line = dict(color = reference,
                                    shape = 'spline',
                                    width = 1)))
fig_AWND.add_trace(go.Scatter(x = df_25_AWND_go["axisdate"],
                         y = df_25_AWND_go["Daily Average"],
                         mode = "lines",
                         name = "2025",
                         connectgaps = True,
                         line = dict(color = hue,
                                     shape = 'spline',
                                     width = 3)))
fig_AWND.update_layout(plot_bgcolor = canvas,
                  paper_bgcolor = canvas,
                  showlegend = True,
                  legend_font_color = hue,
                  legend_orientation = 'h',
                  legend_yanchor = 'top',
                  legend_y = 1.15,
                  legend_xanchor = 'right',
                  legend_x = 1,
                  title = dict(text = "AVERAGE DAILY WIND SPEED",
                               font_color = hue,
                               xanchor = 'left',
                               x = 0.074,
                               font_size = 25,
                               yanchor = 'top',
                               y = 0.84)
                               )
    
fig_AWND.update_xaxes(color = hue,
                gridcolor = hue,
                linecolor = hue,
                mirror = True,
                showgrid = False,
                ticks = "inside",
                ticklen = 5,
                tickformat= "%b %d",
                nticks = 12,
                range = ['2025-01-01', '2025-12-31'],
                title = dict(text = ""),
                )
fig_AWND.update_yaxes(color = hue,
                 gridcolor = hue,
                 linecolor = hue,
                 mirror = True,
                 showgrid = True,
                 ticks = 'inside',
                 ticklen = 5,
                 zeroline = False,
                 rangemode = 'tozero',
                 title = dict(text = "Wind Speed (km/h)")
                 )

fig_AWND.show()

#SN33 / SX33 - Min and Max Soil Temp (Bare ground, depth of 20 cm)

hue = 'slategrey' #line color of graph
canvas = 'whitesmoke' #background color
referencemin = 'lightsteelblue' #color of reference line
referencemax = 'wheat'
mincolor = 'navy'
maxcolor = 'goldenrod'

df_SN33_go = df_SN33_go.sort_values(by="axisdate")
df_SX33_go = df_SX33_go.sort_values(by="axisdate")
df_25_SN33_go = df_25_SN33_go.sort_values(by="axisdate")
df_25_SX33_go = df_25_SX33_go.sort_values(by="axisdate")

fig_SN33 = go.Figure ()
fig_SN33.add_trace(go.Scatter(x = df_SN33_go["axisdate"],
                        y = df_SN33_go["Daily Average"],
                        mode = "lines",
                        name = "Decade (Min)",
                        #connectgaps = False,
                        hoverinfo = 'none',
                        line = dict(color = referencemin,
                                    shape = 'spline',
                                    width = 1)))
fig_SN33.add_trace(go.Scatter(x = df_SX33_go["axisdate"],
                        y = df_SX33_go["Daily Average"],
                        mode = "lines",
                        name = "Decade (Max)",
                        #connectgaps = False,
                        hoverinfo = 'none',
                        line = dict(color = referencemax,
                                    shape = 'spline',
                                    width = 1)))
fig_SN33.add_trace(go.Scatter(x = df_25_SN33_go["axisdate"],
                         y = df_25_SN33_go["Daily Average"],
                         mode = "lines",
                         name = "2025 (Min)",
                         connectgaps = True,
                         line = dict(color = mincolor,
                                     shape = 'spline',
                                     width = 3)))
fig_SN33.add_trace(go.Scatter(x = df_25_SX33_go["axisdate"],
                         y = df_25_SX33_go["Daily Average"],
                         mode = "lines",
                         name = "2025 (Max)",
                         connectgaps = True,
                         line = dict(color = maxcolor,
                                     shape = 'spline',
                                     width = 3)))
fig_SN33.update_layout(plot_bgcolor = canvas,
                  paper_bgcolor = canvas,
                  legend_font_color = hue,
                  legend_orientation = 'v',
                  legend_yanchor = 'top',
                  legend_y = 1,
                  legend_xanchor = 'right',
                  legend_x = 1,
                  title = dict(text = "MAX / MIN SOIL TEMPERATURE",
                               font_color = hue,
                               xanchor = 'left',
                               x = 0.074,
                               font_size = 25,
                               yanchor = 'top',
                               y = 0.84)
                               )
    
fig_SN33.update_xaxes(color = hue,
                gridcolor = hue,
                linecolor = hue,
                mirror = True,
                showgrid = False,
                ticks = "inside",
                ticklen = 5,
                tickformat= "%b %d",
                nticks = 12,
                title = dict(text = ""),
                )
fig_SN33.update_yaxes(color = hue,
                 gridcolor = hue,
                 linecolor = hue,
                 mirror = True,
                 showgrid = True,
                 ticks = 'inside',
                 ticklen = 5,
                 zeroline = False,
                 #rangemode = 'tozero',
                 title = dict(text = "Temperature (C)")
                 )

fig_SN33.show()

#WSFI - HIGHEST GUST SPEED

hue = 'olive' #line color of graph
canvas = 'ivory' #background color
reference = 'darkkhaki' #color of reference line

df_WSFI_go = df_WSFI_go.sort_values(by="axisdate")
df_25_WSFI_go = df_25_WSFI_go.sort_values(by="axisdate")

fig_WSFI = go.Figure ()
fig_WSFI.add_trace(go.Scatter(x = df_WSFI_go["axisdate"],
                        y = df_WSFI_go["Daily Average"],
                        mode = "lines",
                        name = "Decade Average",
                        connectgaps = True,
                        hoverinfo = 'none',
                        line = dict(color = reference,
                                    shape = 'spline',
                                    width = 1)))
fig_WSFI.add_trace(go.Scatter(x = df_25_WSFI_go["axisdate"],
                         y = df_25_WSFI_go["Daily Average"],
                         mode = "lines",
                         name = "2025",
                         connectgaps = True,
                         line = dict(color = hue,
                                     shape = 'spline',
                                     width = 3)))
fig_WSFI.update_layout(plot_bgcolor = canvas,
                  paper_bgcolor = canvas,
                  showlegend = True,
                  legend_font_color = hue,
                  legend_orientation = 'h',
                  legend_yanchor = 'top',
                  legend_y = 1.15,
                  legend_xanchor = 'right',
                  legend_x = 1,
                  title = dict(text = "HIGHEST GUST SPEED",
                               font_color = hue,
                               xanchor = 'left',
                               x = 0.074,
                               font_size = 25,
                               yanchor = 'top',
                               y = 0.84)
                               )
    
fig_WSFI.update_xaxes(color = hue,
                gridcolor = hue,
                linecolor = hue,
                mirror = True,
                showgrid = False,
                ticks = "inside",
                ticklen = 5,
                tickformat= "%b %d",
                nticks = 12,
                range = ['2025-01-01', '2025-12-31'],
                title = dict(text = ""),
                )
fig_WSFI.update_yaxes(color = hue,
                 gridcolor = hue,
                 linecolor = hue,
                 mirror = True,
                 showgrid = True,
                 ticks = 'inside',
                 ticklen = 5,
                 zeroline = False,
                 rangemode = 'tozero',
                 title = dict(text = "Wind Speed (km/h)")
                 )

fig_WSFI.show()

## Dashboard

all_viz = ["fig_PRCP", "fig_SNOW", "fig_SNWD", "fig_WESD", "fig_EVAP", "fig_TMIN", "fig_SN33", "fig_AWND", "fig_WSFI"]

graph1 = fig_PRCP
graph2 = fig_SNOW
graph3 = fig_SNWD
graph4 = fig_WESD
graph5 = fig_EVAP
graph6 = fig_TMIN
graph7 = fig_SN33
graph8 = fig_AWND
graph9 = fig_WSFI

app = dash.Dash(__name__)

app.layout = html.Div(
    id='app-container',
    style={'padding': '20px'},
    children=[
        html.H1(
            "UTAH WEATHER AND CLIMATE",
            id='title-text',
            style={
                'fontFamily': 'Arial, sans-serif',
                'fontSize': '36px',
                'textAlign': 'center',
                'marginBottom': '20px'
            }
        ),
        dcc.Dropdown(
            id='graph-selector',
            options=[{'label': 'Precipitation', 'value': 'graph1'},
                     {'label': 'Snowfall', 'value': 'graph2'},
                     {'label': 'Snow Depth', 'value': 'graph3'},
                     {'label': 'Snow Water Equivalent', 'value': 'graph4'},
                     {'label': 'Evaporation', 'value': 'graph5'},
                     {'label': 'Temperature', 'value': 'graph6'},
                     {'label': 'Soil Temperature', 'value': 'graph7'},
                     {'label': 'Wind Speed', 'value': 'graph8'},
                     {'label': 'Wind Gusts', 'value': 'graph9'}
                     ],
            value='graph1',
            style={
                'width': '200px',
                'backgroundColor': '#f0f0f0',
                'border': '1px solid #aaa',
                'fontFamily': 'Arial, sans-serif',
                'fontSize': '14px',
                'fontWeight': 'normal'
            },
            className='custom-dropdown'
        ),
        dcc.Graph(id='selected-graph'),
        html.Div(id='graph-explanation', style={'marginTop': '30px',
                                                'marginBottom': '30px',
                                                'fontFamily': 'Arial, sans-serif',
                                                'fontSize': '16px', })
    ]
)


@app.callback(
    Output('selected-graph', 'figure'),
    Output('graph-explanation', 'children'),
    Output('graph-explanation', 'style'),
    Output('graph-selector', 'style'),
    Output('app-container', 'style'),
    Output('title-text', 'style'),
    Input('graph-selector', 'value')
)
def update_graph(selected_graph):
    dropdown_style = {
        'width': '200px',
        'fontFamily': 'Arial, sans-serif',
        'fontSize': '14px'
    }
    explanation_style = {'fontFamily': 'Arial, sans-serif', 'marginTop': '30px','marginBottom': '30px'}
    app_style = {'padding': '20px'}
    title_style = {'fontFamily': 'Arial', 'fontSize': '30px','textAlign': 'center', 'marginBottom': '10px'} #create title style.

    if selected_graph == 'graph1':
        textcolor = 'rgb(241,248,254)'
        color = 'rgb(85,129,176)'
        dropdown_style['backgroundColor'] = textcolor
        dropdown_style['color'] = color
        explanation_style['color'] = color
        app_style['backgroundColor'] = 'rgb(220,235,250)'
        title_style['color'] = color #set title color
        return graph1, "This is a measure, in millimeters, of how much water (both rain and snow) has fallen in the last 24 hours. This measurement represents a daily average for the entire state.", explanation_style, dropdown_style, app_style, title_style

    elif selected_graph == 'graph2':
        textcolor = 'rgb(230,220,248)'
        color = 'rgb(70,61,134)'
        dropdown_style['backgroundColor'] = textcolor
        dropdown_style['color'] = color
        explanation_style['color'] = color
        app_style['backgroundColor'] = 'rgb(215,210,240)'
        title_style['color'] = color
        return graph2, "This is a measure, in millimeters,  of how much snow has fallen in the last 24 hours. This measurement represents a daily average for the entire state.", explanation_style, dropdown_style, app_style, title_style

    elif selected_graph == 'graph3':
        textcolor = 'rgb(245,245,245)'
        color = 'rgb(115,127,142)'
        dropdown_style['backgroundColor'] = textcolor
        dropdown_style['color'] = color
        explanation_style['color'] = color
        app_style['backgroundColor'] = 'rgb(235,235,235)'
        title_style['color'] = color
        return graph3, "This is a measure of how deep the snow is, in millimeters. This measurement represents a daily average for the entire state.", explanation_style, dropdown_style, app_style, title_style

    elif selected_graph == 'graph4':
        textcolor = 'rgb(241,248,254)'
        color = 'rgb(85,129,176)'
        dropdown_style['backgroundColor'] = textcolor
        dropdown_style['color'] = color
        explanation_style['color'] = color
        app_style['backgroundColor'] = 'rgb(220,235,250)'
        title_style['color'] = color
        return graph4, "Snow water equivalent (SWE) is a measure of how much water would be produced if the snow were to melt, here recorded in millimeters. A higher SWE means a heavier, wetter snow. This measurement represents a daily average for the entire state.", explanation_style, dropdown_style, app_style, title_style

    elif selected_graph == 'graph5':
        textcolor = 'rgb(243,255,255)'
        color = 'rgb(55,126,127)'
        dropdown_style['backgroundColor'] = textcolor
        dropdown_style['color'] = color
        explanation_style['color'] = color
        app_style['backgroundColor'] = 'rgb(220,240,240)'
        title_style['color'] = color
        return graph5, "This is a measure, in millimeters, of how much water is lost due to natural evaporation over the course of 24 hours. Evaporation is measured by placing a pan of water in a sunny area and measuring how much is lost over time. In the environment, water loss due to evaporation can take place in water bodies, the soil, and even plants. Evaporation can be very rapid under hot and dry conditions. This measurement represents a daily average for the entire state.", explanation_style, dropdown_style, app_style, title_style

    elif selected_graph == 'graph6':
        textcolor = 'rgb(245,245,245)'
        color = 'rgb(115,127,142)'
        dropdown_style['backgroundColor'] = textcolor
        dropdown_style['color'] = color
        explanation_style['color'] = color
        app_style['backgroundColor'] = 'rgb(235,235,235)'
        title_style['color'] = color
        return graph6, "This is a measure, in Celsius, of the maximum and minimum daily air temperatures. These measurements represent daily averages for the entire state.", explanation_style, dropdown_style, app_style, title_style

    elif selected_graph == 'graph7':
        textcolor = 'rgb(245,245,245)'
        color = 'rgb(115,127,142)'
        dropdown_style['backgroundColor'] = textcolor
        dropdown_style['color'] = color
        explanation_style['color'] = color
        app_style['backgroundColor'] = 'rgb(235,235,235)'
        title_style['color'] = color
        return graph7, "This is a measure, in Celsius, of the maximum and minimum daily soil temperatures. Measurements were taken on bare soil at a depth of 20 cm. These measurements represent daily averages for the entire state.", explanation_style, dropdown_style, app_style, title_style

    elif selected_graph == 'graph8':
        textcolor = 'rgb(243,255,241)'
        color = 'rgb(41,98,24)'
        dropdown_style['backgroundColor'] = textcolor
        dropdown_style['color'] = color
        explanation_style['color'] = color
        app_style['backgroundColor'] = 'rgb(220,240,220)'
        title_style['color'] = color
        return graph8, "This is a measure, in kilometers per hour, of the average daily wind speed. This measurement represents a daily average for the entire state.", explanation_style, dropdown_style, app_style, title_style

    elif selected_graph == 'graph9':
        textcolor = 'rgb(255,255,241)'
        color = 'rgb(128,128,38)'
        dropdown_style['backgroundColor'] = textcolor
        dropdown_style['color'] = color
        explanation_style['color'] = color
        app_style['backgroundColor'] = 'rgb(240,240,220)'
        title_style['color'] = color
        return graph9, "This is a measure, in kilometers per hour, of the maximum daily wind speed. Individual wind gusts can be considerably faster and more destructive than the average daily wind speed. This measurement represents a daily average of maximum gust speed for the entire state.", explanation_style, dropdown_style, app_style, title_style

    else:
        dropdown_style['backgroundColor'] = 'white'
        dropdown_style['color'] = 'black'
        explanation_style['color'] = 'black'
        app_style['backgroundColor'] = 'rgb(240,240,240)'
        title_style['color'] = 'black'
        return {}, "", explanation_style, dropdown_style, app_style, title_style

if __name__ == '__main__':
    app.run_server(debug=True)