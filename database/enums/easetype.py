from enum import Enum

class EaseType(Enum):
	NONE = "NONE"
	LINEAR = "Linear"
	QUADRATIC = "Quad"
	CUBIC = "Cubic"
	QUARTIC = "Quart"
	QUINTIC = "Quint"
	SINUSOIDAL = "Sine"
	EXPONENTIAL = "Expo"
	CIRCULAR = "Circ"
	ELASTIC = "Elastic"
	BACK = "Back"
	BOUNCE = "Bounce"
	STEPPED = "Stepped"
