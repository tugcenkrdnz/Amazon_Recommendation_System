import streamlit as st
import joblib

st.set_page_config(page_title="Amazon Öneri Sistemi", page_icon="🛒")

st.title("🛒 Amazon Akıllı Öneri Sistemi")
st.markdown("---")

# 1. Veriyi Yükle
data = joblib.load('amazon_recommender_package.pkl')
df = data['main_data']

# 2. Giriş Al - Açıklayıcı metin ekledik
st.subheader("Ürün Araması")
asin = st.text_input("Lütfen analiz edilecek Ürün Kodunu (ASIN) giriniz:", "B004PVRGXO")

if st.button("Önerileri Getir"):
    # Filtreleme: Bu ürünü alanların aldığı DİĞER ürünler
    users = df[df['item'] == asin]['user']
    recs = df[df['user'].isin(users) & (df['item'] != asin)]
    
    if not recs.empty:
        # Başlık ekliyoruz ki kullanıcı neye baktığını bilsin
        st.success(f"🔍 '{asin}' kodlu ürünü alan müşterilerimiz, aşağıdaki yüksek puanlı ürünleri de tercih etti:")
        
        # En yüksek puanlı ilk 3 benzersiz ürün
        res = recs[['item', 'average_rating']].drop_duplicates().sort_values('average_rating', ascending=False).head(3)
        
        # Tabloyu güzelleştirelim - Sütun isimlerini Türkçeleştirelim
        res.columns = ['Önerilen Ürün Kodu', 'Müşteri Memnuniyet Puanı']
        
        # İndeks numarasını (resimdeki o karmaşık sayıları) gizleyerek tabloyu basalım
        st.table(res.reset_index(drop=True))
        
        st.info("💡 İpucu: Ürün kodlarını kopyalayıp Amazon üzerinde aratarak ürün detaylarına ulaşabilirsiniz.")
    else:
        st.warning("Üzgünüz, bu ürün için yeterli satın alma verisi bulunamadı veya kod hatalı.")