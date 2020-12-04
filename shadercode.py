# Shader功能
# -*- encoding:utf8 -*-

def addColorProperty():
    text = '''float4 colorParam: PsParam1
<   bool artistEditable = true;
    string UIName = "颜色";
    string UIDesc = "这是一个颜色属性";
    string UIFormat = "R[0:1],G[0:1],B[0:1],A[0:1]";
    string UIWidget = "Color";
> = float4(1, 1, 1, 1);
'''
    return text

def addFloat1Property():
    text = '''float floatParam : PsParam1
<   bool artistEditable = true;
	string UIName = "float参数";
	string UIDesc = "这是一个float参数";
	float UIMin = 0;
	float UIMax = 1;
	int UIDigits = 1;
> = 1.0;
'''
    return text

def addFloat2Property():
    text = '''float2 float2Params : PsParam1
<   bool artistEditable = true;
	string UIName = "float2参数";
	string UIDesc = "这是一个float2参数";
	string UIFormat = "参数X[0.0:1.0],参数Y[0.0:1.0]";
> = float2(1.0, 1.0);
'''
    return text

def addFloat3Property():
    text = '''float3 float3Params : PsParam1
<   bool artistEditable = true;
	string UIName = "float3参数";
	string UIDesc = "这是一个float3参数";
	string UIFormat = "参数X[0.0:1.0],参数Y[0.0:1.0],参数Z[0.0:1.0]";
> = float3(1.0, 1.0, 1.0);
'''
    return text

def addFloat4Property():
    text = '''float4 float4Params : PsParam1
<   bool artistEditable = true;
    string UIName = "float4参数";
	string UIDesc = "这是一个float4参数";
	string UIFormat = "参数X[0.0:1.0],参数Y[0.0:1.0],参数Z[0.0:1.0],参数W[0.0:1.0]";
> = float4(1.0, 1.0, 1.0, 1.0);
'''
    return text

def addTextureProperty():
    text = '''texture texMap
<   bool artistEditable = true;
	string UIName = "纹理贴图";
	string UIDesc = "这是一张纹理贴图";
>;
sampler texMapSampler : register(s1)
<   string tex="texMap";
	int address=SamplerAddress_Wrap;
	int filter=SamplerFilter_Linear;
> = sampler_state { 
	REGULAR_SAMPLER(texMap);
};
'''
    return text

def addSchlickFresnelFunction():
    text = '''// Schlick菲涅尔近似
float SchlickFresnel(float3 N, float3 V, float F0, float Power)
{
    // Power Default Value = 5.0
    return saturate(F0 + (1.0 - F0) * pow(1.0 - dot(N, V), Power));
}
'''
    return text

def addRGB2HSVFunction():
    text = '''// RGB转HSV
half3 RGBtoHSV(half3 args){
	half4 K = half4(0.0, -1.0 / 3.0, 2.0 / 3.0, -1.0);
	half4 p = lerp(half4(args.bg, K.wz), half4(args.gb, K.xy), step(args.b, args.g));
	half4 q = lerp(half4(p.xyw, args.r), half4(args.r, p.yzx), step(p.x, args.r));

	half d = q.x - min(q.w, q.y);
	half e = 1.0e-10;
	return half3(abs(q.z + (q.w - q.y) / (6.0 * d + e)), d / (q.x + e), q.x);
}
'''
    return text

def addHSV2RGBFunction():
    text = '''// HSV转RGB
half3 HSVtoRGB(half3 args)
{
    half4 K = half4(1.0, 2.0 / 3.0, 1.0 / 3.0, 3.0);
    half3 P = abs(frac(args.xxx + K.xyz) * 6.0 - K.www);
    return args.z * lerp(K.xxx, saturate(P - K.xxx), args.y);
}
'''
    return text

def addPseudoRandomFunction():
    text = '''// 伪随机数 Pseudo Randomness
float PseudoRandom( float2 p )
{
    float2 K1 = float2(
        23.14069263277926, // e^pi (Gelfond's constant)
         2.665144142690225 // 2^sqrt(2) (Gelfond's Schneider constant)
    );
    return frac( cos( dot(p,K1) ) * 12345.6789 );
}
'''
    return text

def addClassic2DPerlinNoiseFunction():
    text = '''// 经典2D柏林噪声 Classic Perlin 2D Noise 
float4 permute(float4 x){
    return fmod(((x*34.0)+1.0)*x, 289.0);
}
float2 fade(float2 t) {
    return t*t*t*(t*(t*6.0-15.0)+10.0);
}
float ClassicPerlin2DNoise(float2 P){
    float4 Pi = floor(P.xyxy) + float4(0.0, 0.0, 1.0, 1.0);
    float4 Pf = frac(P.xyxy) - float4(0.0, 0.0, 1.0, 1.0);
    Pi = fmod(Pi, 289.0); // To avoid truncation effects in permutation
    float4 ix = Pi.xzxz;
    float4 iy = Pi.yyww;
    float4 fx = Pf.xzxz;
    float4 fy = Pf.yyww;
    float4 i = permute(permute(ix) + iy);
    float4 gx = 2.0 * frac(i * 0.0243902439) - 1.0; // 1/41 = 0.024...
    float4 gy = abs(gx) - 0.5;
    float4 tx = floor(gx + 0.5);
    gx = gx - tx;
    float2 g00 = float2(gx.x,gy.x);
    float2 g10 = float2(gx.y,gy.y);
    float2 g01 = float2(gx.z,gy.z);
    float2 g11 = float2(gx.w,gy.w);
    float4 norm = 1.79284291400159 - 0.85373472095314 * 
    float4(dot(g00, g00), dot(g01, g01), dot(g10, g10), dot(g11, g11));
    g00 *= norm.x;
    g01 *= norm.y;
    g10 *= norm.z;
    g11 *= norm.w;
    float n00 = dot(g00, float2(fx.x, fy.x));
    float n10 = dot(g10, float2(fx.y, fy.y));
    float n01 = dot(g01, float2(fx.z, fy.z));
    float n11 = dot(g11, float2(fx.w, fy.w));
    float2 fade_xy = fade(Pf.xy);
    float2 n_x = lerp(float2(n00, n01), float2(n10, n11), fade_xy.x);
    float n_xy = lerp(n_x.x, n_x.y, fade_xy.y);
    return 2.3 * n_xy;
}
'''
    return text